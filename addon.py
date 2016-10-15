import xbmcplugin,xbmcgui

__addon__ = "Intergalactic FM"
__addonid__ = "plugin.audio.intergalacticfm"
__version__ = "0.0.3"

def log(msg):
    print "[PLUGIN] '%s (%s)' " % (__addon__, __version__) + str(msg)

log("Initialized!")

handle = int(sys.argv[1])
query = sys.argv[2]

channels = [
	[ "IFM MAIN", "Electro & Wave", "http://radio.intergalacticfm.com/1.m3u", "https://intergalacticfm.com/images/AppIFM1-100.png" ],
	[ "DISCO FETISH", "Italo, Disco & Oldschool", "http://radio.intergalacticfm.com/2.m3u", "https://intergalacticfm.com/images/AppIFM2-100.png" ],
	[ "THE DREAM MACHINE", "Soundtracks & Exotica", "http://radio.intergalacticfm.com/4.m3u", "https://intergalacticfm.com/images/AppIFM4-100.png" ],
	[ "THE GARDEN", "Space & Ambient", "http://radio.intergalacticfm.com/5.m3u", "https://intergalacticfm.com/images/AppIFM5-100.png" ],
	[ "INTERGALACTIC TV", "IFM TELEVISION", "rtmp://intergalactic.tv/live/prc", "https://intergalacticfm.com/images/AppIFM3-100.png" ]
	]

for x in channels:
	li = xbmcgui.ListItem(x[0], x[1], thumbnailImage=x[3])
	li.setProperty("IsPlayable","true")
	xbmcplugin.addDirectoryItem(handle=handle,url=x[2],listitem=li)

xbmcplugin.endOfDirectory(handle)
