dmapCodeTypes = {
    #'f\x8dch': ('dmap.haschildcontainers', 'b'),
    'abal': ('daap.browsealbumlisting', 'c'),
    'abar': ('daap.browseartistlisting', 'c'),
    'abcp': ('daap.browsecomposerlisting', 'c'),
    'abgn': ('daap.browsegenrelisting', 'c'),
    'abpl': ('daap.baseplaylist', 'b'),
    'abro': ('daap.databasebrowse', 'c'),
    'adbs': ('daap.databasesongs', 'c'),
    'aeAI': ('com.apple.itunes.itms-artistid', 'i'),
    'aeCI': ('com.apple.itunes.itms-composerid', 'i'),
    'aeEN': ('com.apple.itunes.episode-num-str', 's'),
    'aeES': ('com.apple.itunes.episode-sort', 'i'),
    'aeFP': ('com.apple.itunes.req-fplay', 'b'),
    'aeGU': ('com.apple.itunes.gapless-dur', 'l'),
    'aeGD': ('com.apple.itunes.gapless-enc-dr', 'i'),
    'aeGE': ('com.apple.itunes.gapless-enc-del', 'i'),
    'aeGH': ('com.apple.itunes.gapless-heur', 'i'),
    'aeGI': ('com.apple.itunes.itms-genreid', 'i'),
    'aeGR': ('com.apple.itunes.gapless-resy', 'l'),
    'aeHV': ('com.apple.itunes.has-video', 'b'),
    'aeMK': ('com.apple.itunes.mediakind', 'b'),
    'aeNN': ('com.apple.itunes.network-name', 's'),
    'aeNV': ('com.apple.itunes.norm-volume', 'i'),
    'aePC': ('com.apple.itunes.is-podcast', 'b'),
    'aePI': ('com.apple.itunes.itms-playlistid', 'i'),
    'aePP': ('com.apple.itunes.is-podcast-playlist', 'b'),
    'aePS': ('com.apple.itunes.special-playlist', 'b'),
    'aeSU': ('com.apple.itunes.season-num', 'i'),
    'aeSF': ('com.apple.itunes.itms-storefrontid', 'i'),
    'aeSI': ('com.apple.itunes.itms-songid', 'i'),
    'aeSN': ('com.apple.itunes.series-name', 's'),
    'aeSP': ('com.apple.itunes.smart-playlist', 'b'),
    'aeSV': ('com.apple.itunes.music-sharing-version', 'i'),
    'agrp': ('daap.songgrouping', 's'),
    'aply': ('daap.databaseplaylists', 'c'),
    'aprm': ('daap.playlistrepeatmode', 'b'),
    'apro': ('daap.protocolversion', 'v'),
    'apsm': ('daap.playlistshufflemode', 'b'),
    'apso': ('daap.playlistsongs', 'c'),
    'arif': ('daap.resolveinfo', 'c'),
    'arsv': ('daap.resolve', 'c'),
    'asaa': ('daap.songalbumartist', 's'),
    'asal': ('daap.songalbum', 's'),
    'asar': ('daap.songartist', 's'),
    'asbk': ('daap.bookmarkable', 'b'),
    'asbo': ('daap.songbookmark', 'i'),
    'asbr': ('daap.songbitrate', 'h'),
    'asbt': ('daap.songbeatsperminute', 'h'),
    'ascd': ('daap.songcodectype', 'i'),
    'ascm': ('daap.songcomment', 's'),
    'ascn': ('daap.songcontentdescription', 's'),
    'asco': ('daap.songcompilation', 'b'),
    'ascp': ('daap.songcomposer', 's'),
    'ascr': ('daap.songcontentrating', 'b'),
    'ascs': ('daap.songcodecsubtype', 'i'),
    'asct': ('daap.songcategory', 's'),
    'asda': ('daap.songdateadded', 't'),
    'asdb': ('daap.songdisabled', 'b'),
    'asdc': ('daap.songdisccount', 'h'),
    'asdk': ('daap.songdatakind', 'b'),
    'asdm': ('daap.songdatemodified', 't'),
    'asdn': ('daap.songdiscnumber', 'h'),
    'asdp': ('daap.songdatepurchased', 't'),
    'asdr': ('daap.songdatereleased', 't'),
    'asdt': ('daap.songdescription', 's'),
    'ased': ('daap.songextradata', 'h'),
    'aseq': ('daap.songeqpreset', 's'),
    'asfm': ('daap.songformat', 's'),
    'asgn': ('daap.songgenre', 's'),
    'asgp': ('daap.songgapless', 'b'),
    'ashp': ('daap.songhasbeenplayed', 'b'),
    'asky': ('daap.songkeywords', 's'),
    'aslc': ('daap.songlongcontentdescription', 's'),
    'asrv': ('daap.songrelativevolume', 'ub'),
    'assu': ('daap.sortalbum', 's'),
    'assa': ('daap.sortartist', 's'),
    'assc': ('daap.sortcomposer', 's'),
    'assl': ('daap.sortalbumartist', 's'),
    'assn': ('daap.sortname', 's'),
    'assp': ('daap.songstoptime', 'i'),
    'assr': ('daap.songsamplerate', 'i'),
    'asss': ('daap.sortseriesname', 's'),
    'asst': ('daap.songstarttime', 'i'),
    'assz': ('daap.songsize', 'i'),
    'astc': ('daap.songtrackcount', 'h'),
    'astm': ('daap.songtime', 'i'),
    'astn': ('daap.songtracknumber', 'h'),
    'asul': ('daap.songdataurl', 's'),
    'asur': ('daap.songuserrating', 'b'),
    'asyr': ('daap.songyear', 'h'),
    'ated': ('daap.supportsextradata', 'h'),
    'avdb': ('daap.serverdatabases', 'c'),
    'mbcl': ('dmap.bag', 'c'),
    'mccr': ('dmap.contentcodesresponse', 'c'),
    'mcna': ('dmap.contentcodesname', 's'),
    'mcnm': ('dmap.contentcodesnumber', 'i'),
    'mcon': ('dmap.container', 'c'),
    'mctc': ('dmap.containercount', 'i'),
    'mcti': ('dmap.containeritemid', 'i'),
    'mcty': ('dmap.contentcodestype', 'h'),
    'mdcl': ('dmap.dictionary', 'c'),
    'miid': ('dmap.itemid', 'i'),
    'mikd': ('dmap.itemkind', 'b'),
    'mimc': ('dmap.itemcount', 'i'),
    'minm': ('dmap.itemname', 's'),
    'mlcl': ('dmap.listing', 'c'),
    'mlid': ('dmap.sessionid', 'i'),
    'mlit': ('dmap.listingitem', 'c'),
    'mlog': ('dmap.loginresponse', 'c'),
    'mpco': ('dmap.parentcontainerid', 'i'),
    'mper': ('dmap.persistentid', 'l'),
    'mpro': ('dmap.protocolversion', 'v'),
    'mrco': ('dmap.returnedcount', 'i'),
    'msau': ('dmap.authenticationmethod', 'b'),
    'msal': ('dmap.supportsautologout', 'b'),
    'msas': ('dmap.authenticationschemes', 'i'),
    'msbr': ('dmap.supportsbrowse', 'b'),
    'msdc': ('dmap.databasescount', 'i'),
    'msex': ('dmap.supportsextensions', 'b'),
    'msix': ('dmap.supportsindex', 'b'),
    'mslr': ('dmap.loginrequired', 'b'),
    'mspi': ('dmap.supportspersistentids', 'b'),
    'msqy': ('dmap.supportsquery', 'b'),
    'msrs': ('dmap.supportsresolve', 'b'),
    'msrv': ('dmap.serverinforesponse', 'c'),
    'mstc': ('dmap.utctime', 't'),
    'mstm': ('dmap.timeoutinterval', 'i'),
    'msto': ('dmap.utcoffset', 'ui'),
    'msts': ('dmap.statusstring', 's'),
    'mstt': ('dmap.status', 'i'),
    'msup': ('dmap.supportsupdate', 'b'),
    'mtco': ('dmap.specifiedtotalcount', 'i'),
    'mudl': ('dmap.deletedidlisting', 'c'),
    'mupd': ('dmap.updateresponse', 'c'),
    'musr': ('dmap.serverrevision', 'i'),
    'muty': ('dmap.updatetype', 'b'),
    'ppro': ('dpap.protocolversion', 'i'),
    'pret': ('dpap.unknown', 'c'),
}

dmapDataTypes = {
    1: 'b',  # byte
    2: 'ub',  # unsigned byte
    3: 'h',  # short
    4: 'uh',  # unsigned short
    5: 'i',  # integer
    6: 'ui',  # unsigned integer
    7: 'l',  # long
    8: 'ul',  # unsigned long
    9: 's',  # string
    10: 't',  # timestamp
    11: 'v',  # version
    12: 'c',  # container
}

dmapNames = {}
for k in dmapCodeTypes.keys():
    dmapNames[dmapCodeTypes[k][0]] = k

dmapReverseDataTypes = {}
for k in dmapDataTypes.keys():
    dmapReverseDataTypes[dmapDataTypes[k]] = k
