#!/usr/bin/env python
#Copyright (C) 2008 Erik Hetzner

#This file is part of Spydaap. Spydaap is free software: you can
#redistribute it and/or modify it under the terms of the GNU General
#Public License as published by the Free Software Foundation, either
#version 3 of the License, or (at your option) any later version.

#Spydaap is distributed in the hope that it will be useful, but
#WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with Spydaap. If not, see <http://www.gnu.org/licenses/>.

import web, sys, os, struct, re, select, signal
import spydaap.daap, spydaap.metadata, spydaap.containers, spydaap.cache
from spydaap.daap import do
import config

try:
    import pybonjour
    bonjour = True
    print 'pybonjour detected.'
except:
    bonjour = False
    print 'pybonjour not found, trying python-avahi.'
    try:
        from ZeroconfService import ZeroconfService
        avahi = True
        print 'python-avahi detected.'
    except:
        avahi = False
        print 'python-avahi not found, you need pybonjour or python-avahi+python-dbus to get Zeroconf Service Publishing.'


#itunes sends request for:
#GET daap://192.168.1.4:3689/databases/1/items/626.mp3?seesion-id=1
#so we must hack the urls; annoying.


itunes_re = '(?://[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}:[0-9]+)?'
drop_q = '(?:\\?.*)?'
urls = (
    itunes_re + '/', 
    'server_info', #
    itunes_re + '/server-info', 
    'server_info', #
    '/content-codes', 
    'content_codes', #
    '/databases', 
    'database_list', #
    '/databases/([0-9]+)/items', 
    'item_list', #
    itunes_re + '/databases/([0-9]+)/items/([0-9]+)\\.([0-9a-z]+)' + drop_q, 
    'item', #
    '/databases/([0-9]+)/containers', 
    'container_list', #
    itunes_re + '/databases/([0-9]+)/containers/([0-9]+)/items', 
    'container_item_list', #
    '/login', 
    'login', #
    '/logout', 
    'logout', #
    '/update',
    'update', #
    )

cache = spydaap.cache.Cache(spydaap.cache_dir)
md_cache = spydaap.metadata.MetadataCache(os.path.join(spydaap.cache_dir, "media"))
container_cache = spydaap.containers.ContainerCache(os.path.join(spydaap.cache_dir, "containers"))

class daap_handler:
    def h(self,web,data,type='application/x-dmap-tagged'):
        web.header('Content-Type', type)
        web.header('DAAP-Server', 'Simple')
        web.header('Expires', '-1')
        web.header('Cache-Control', 'no-cache')
        web.header('Accept-Ranges', 'bytes')
        web.header('Content-Language', 'en_us')
        if (hasattr(data, 'next')):
            try:
                web.header("Content-Length", str(os.stat(data.name).st_size))
            except: pass
            return data
        else:
            try:
                web.header("Content-Length", str(len(data)))
            except: pass
            #sys.stdout.write(data)
            return data

session_id = 1
class login(daap_handler):
    def GET(self):
        mlog = do('dmap.loginresponse',
                  [ do('dmap.status', 200),
                    do('dmap.sessionid', session_id) ])
        return self.h(web,mlog.encode())

class logout:
    def GET(self):
        web.ctx.status = '204 No Content'

class server_info(daap_handler):
    def GET(self):
        msrv = do('dmap.serverinforesponse',
                  [ do('dmap.status', 200),
                    do('dmap.protocolversion', '2.0'),
                    do('daap.protocolversion', '3.0'),
                    do('dmap.timeoutinterval', 1800),
                    do('dmap.itemname', spydaap.server_name),
                    do('dmap.loginrequired', 0),
                    do('dmap.authenticationmethod', 0),
                    do('dmap.supportsextensions', 0),
                    do('dmap.supportsindex', 0),
                    do('dmap.supportsbrowse', 0),
                    do('dmap.supportsquery', 0),
                    do('dmap.supportspersistentids', 0),
                    do('dmap.databasescount', 1),                
                    #do('dmap.supportsautologout', 0),
                    #do('dmap.supportsupdate', 0),
                    #do('dmap.supportsresolve', 0),
                   ])
        return self.h(web,msrv.encode())

class content_codes(daap_handler):
    def GET(self):
        children = [ do('dmap.status', 200) ]
        for code in spydaap.daap.dmapCodeTypes.keys():
            (name, dtype) = spydaap.daap.dmapCodeTypes[code]
            d = do('dmap.dictionary',
                   [ do('dmap.contentcodesnumber', code),
                     do('dmap.contentcodesname', name),
                     do('dmap.contentcodestype',
                        spydaap.daap.dmapReverseDataTypes[dtype])
                     ])
            children.append(d)
        mccr = do('dmap.contentcodesresponse',
                  children)
        return self.h(web, mccr.encode())

class database_list(daap_handler):
    def GET(self):
        d = do('daap.serverdatabases',
               [ do('dmap.status', 200),
                 do('dmap.updatetype', 0),
                 do('dmap.specifiedtotalcount', 1),
                 do('dmap.returnedcount', 1),
                 do('dmap.listing',
                    [ do('dmap.listingitem',
                         [ do('dmap.itemid', 1),
                           do('dmap.persistentid', 1),
                           do('dmap.itemname', spydaap.server_name),
                           do('dmap.itemcount', 
                              len(md_cache)),
                           do('dmap.containercount', len(container_cache))])
                      ])
                 ])
        return self.h(web,d.encode())

class item_list(daap_handler):
    def GET(self,database_id):
        def build_item(md):
            return do('dmap.listingitem', 
                      [ do('dmap.itemkind', 2),
                        do('dmap.containeritemid', md.id),
                        do('dmap.itemid', md.id),
                        md.get_dmap_raw()
                        ])
        def build(f):
            children = [ build_item (md) for md in md_cache ]
            file_count = len(children)
            d = do('daap.databasesongs',
                   [ do('dmap.status', 200),
                     do('dmap.updatetype', 0),
                     do('dmap.specifiedtotalcount', file_count),
                     do('dmap.returnedcount', file_count),
                     do('dmap.listing',
                        children) ])
            f.write(d.encode())
        return self.h(web, cache.get('item_list', build))

server_revision = 1

class update(daap_handler):
    def GET(self):
        mupd = do('dmap.updateresponse',
                  [ do('dmap.status', 200),
                    do('dmap.serverrevision', server_revision),
                    ])
        return self.h(web, mupd.encode())

class ContentRangeFile:
    def __init__(self, parent, start, end=None, chunk=1024):
        self.parent = parent
        self.start = start
        self.end = end
        self.chunk = chunk
        self.parent.seek(self.start)
        self.read = start

    def next(self):
        to_read = self.chunk
        if (self.end != None):
            if (self.read >= self.end):
                self.parent.close()
                raise StopIteration
            if (to_read + self.read > self.end):
                to_read = self.end - self.read
            retval = self.parent.read(to_read)
            self.read = self.read + len(retval)
        else: retval = self.parent.read(to_read)
        if retval == '':
            self.parent.close()
            raise StopIteration
        else: return retval

    def __iter__(self):
        return self

class item(daap_handler):
    def GET(self,database,item,format):
        fn = md_cache.get_item_by_id(item).get_original_filename()
        if (web.ctx.environ.has_key('HTTP_RANGE')):
            rs = web.ctx.environ['HTTP_RANGE']
            m = re.compile('bytes=([0-9]+)-([0-9]+)?').match(rs)
            (start, end) = m.groups()
            if end != None: end = int(end)
            else: end = os.stat(fn).st_size
            start = int(start)
            f = ContentRangeFile(open(fn), start, end)
            web.ctx.status = "206 Partial Content"
            web.header("Content-Range", 
                       "bytes " + str(start) + "-"
                       + str(end) + "/"
                       + str(os.stat(fn).st_size))
        else: f = open(fn)
        return self.h(web, f, 'audio/*')

class container_list(daap_handler):
    def GET(self,database):
        container_do = []
        for i, c in enumerate(container_cache):
            d = [ do('dmap.itemid', i + 1 ),
                  do('dmap.itemcount', len(c)),
                  do('dmap.containeritemid', i + 1),
                  do('dmap.itemname', c.get_name()) ]
            if c.get_name() == 'Library': # this should be better
                d.append(do('daap.baseplaylist', 1))
            else:
                d.append(do('com.apple.itunes.smart-playlist', 1))
            container_do.append(do('dmap.listingitem', d))
        d = do('daap.databaseplaylists',
               [ do('dmap.status', 200),
                 do('dmap.updatetype', 0),
                 do('dmap.specifiedtotalcount', len(container_do)),
                 do('dmap.returnedcount', len(container_do)),
                 do('dmap.listing',
                    container_do)
                 ])
        return self.h(web, d.encode())

class container_item_list(daap_handler):
    def GET(self, database_id, container_id):
        container = container_cache.get_item_by_id(container_id)
        return self.h(web, container.get_daap_raw())

def rebuild_cache(signum=None, frame=None):
    md_cache.build(spydaap.media_path)
    container_cache.clean()
    container_cache.build(md_cache)
    cache.clean()

rebuild_cache()
signal.signal(signal.SIGHUP, rebuild_cache)

def register_callback(sdRef, flags, errorCode, name, regtype, domain):
    pass

if bonjour:
    #records as in mt-daapd
    myTxtRecord=pybonjour.TXTRecord()
    myTxtRecord['txtvers'] = '1'
    myTxtRecord['iTSh Version'] = '131073'
    myTxtRecord['Machine Name'] = spydaap.server_name
    myTxtRecord['Password'] = 'false'
    #myTxtRecord['Database ID'] = ''
    #myTxtRecord['Version'] = ''
    #myTxtRecord['Machine ID'] = ''
    #myTxtRecord['ffid'] = ''
    
    sdRef = pybonjour.DNSServiceRegister(name = spydaap.server_name,
                                     regtype = "_daap._tcp",
                                     port = spydaap.port,
                                     callBack = register_callback,
                                     txtRecord=myTxtRecord)

    while True:
        ready = select.select([sdRef], [], [])
        if sdRef in ready[0]:
            pybonjour.DNSServiceProcessResult(sdRef)
            break

elif avahi:
    service = ZeroconfService(name=spydaap.server_name,
                                      port=spydaap.port,  stype="_daap._tcp")

    service.publish()

#hacky; there is a better way
sys.argv.append(str(spydaap.port))

web.webapi.internalerror = web.debugerror
#if __name__ == "__main__": web.run(urls, globals())
#web.wsgi.runwsgi(web.webapi.wsgifunc(web.webpyfunc(urls, globals())))
app = web.application(urls, globals())
app.run()


if bonjour:
    sdRef.close()
elif avahi:
    service.unpublish()
