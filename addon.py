import xbmcplugin,xbmcgui

__addon__ = "Intergalactic FM"
__addonid__ = "plugin.audio.intergalacticfm"
__version__ = "0.0.2"

def log(msg):
    print "[PLUGIN] '%s (%s)' " % (__addon__, __version__) + str(msg)

log("Initialized!")

handle = int(sys.argv[1])
query = sys.argv[2]

title = [
    "",
    "MURDERCAPITAL FM", 
    "INTERGALACTIC CLASSIX", 
    "ALIEN BROADCASTERS", 
    "THE DREAM MACHINE", 
    "THE GARDEN",
    ]
description=[
    "",
    "Electro & Wave",
    "Italo, Disco & Oldschool",
    "House & Electronics",
    "Soundtracks & Exotica",
    "Space & Ambient",
    ]

for x in range(1,6):
    img="https://intergalacticfm.com/images/AppIFM"+ str(x) + "-100.png"
    url="http://radio.intergalacticfm.com/%d.m3u" %x
    li = xbmcgui.ListItem(title[x], description[x], thumbnailImage=img)
    li.setProperty("IsPlayable","true")
    xbmcplugin.addDirectoryItem(handle=handle,url=url,listitem=li)

xbmcplugin.endOfDirectory(handle)
