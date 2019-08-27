# import the kodi python modules we are going to use
# see the kodi api docs to find out what functionality each module provides
import xbmc
import xbmcaddon
import sys
import addon

# getting the assetTYPE so we can later confirm that it's a movie or tvshow

assetTYPE = xbmc.getInfoLabel('ListItem.DBtype')

#calling the main function if assetTYPE is movie or tvshow

if assetTYPE == 'movie' or assetTYPE == 'tvshow':
    addon.main();
else:
   assetMsg = "Invalid item selected: '%s'" % assetTYPE
   xbmc.executebuiltin("Notification(\"Tag Quick Edit\", \"%s\")" % assetMsg)