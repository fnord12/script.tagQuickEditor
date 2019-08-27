# kodi.script.tagQuick Editor

This is a branch of the context.tags add-on created by zosky.  I wanted to make a version that could be called as a script.  

The main use case being having the ability to map the script to a keyboard key in your keymap.xml file:

<t>RunScript(script.tagQuickEditor)</t>

This branch also incorporates a few minor updates that were introduced via the Kodi forum topic 
(https://forum.kodi.tv/showthread.php?tid=310752 ) or zosky's add-on but which haven't yet made it into zorsky's build:

- sorting the tags alphabetically (provided by thlucas)
- Displaying the selected Movie/Show name in the pop-up window instead of the generic Select Tags

This build does NOT incorporate thlucas' fix handling the situation where no tags have yet been created.  At least one tag
has to be created via Kodi's normal interface before this will work.


zorsky's original README text follows:


here is an addon that will put a new item under the manage context menu for movies and tvshows. 

my motivation was to separate our massive movie & tv collections into 4 sections, for the wife, kid, me, and  the whole family. the current system is far too cumbersome. i built this for me, but perhaps others might like it too. 

# WARNING - Use At Your Own Risk
i take no responsibility for anything that happens. if your cat has babies, if your plants become sentient or if your library gets borked. i might be able to help, but i can't promise. the best thing to do is always make a backup. 

# what it does
- pulls a list of tags currently in the db
- compares that with those of the item currently selected
- presents a multi-select box to modify the selection
- saves your selections back into the DB

# TODO
suggestions are welcome, pull requests preferred. it does exactly what i want it to
- perhaps add the ability to create new tags ?

# Download and install
- grab the [zip file](https://github.com/zosky/kodi.context.tags/archive/master.zip)
- install in kodi ( settings > addons > install from zip )
