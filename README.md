# RhasspyFiles
misc. files for Rhasspy voice assistant.


## sentences.ini
Sentences file for intents.

These are the different intents created.  I have roughly grouped them with spacing so you can tell similar commands.

  
## profile.json
Profile for configuration.


## /slots/zones
Slot with house zones for automations.

These zones are used in intent sentences for lighting and vacuum automation.


## /slot_programs/songs.py
Songs slot program.

This scans the sub-directories for files and generates a slot with the following design `songname:filepath`.

The song name has the directory and file extension stripped.  Underscores are also replaced with spaces to allow for voice recognition of the song name.
Song files must not contain apostrophes, commas, or other special characters.


## custom_handler.py
Custom intent handler for Rhasspy.

Currently setup with three intents:
  1) The first adjusted the speaker volume (change card to match your systems speaker device).
  2) The second is used to play local mp3 files through the speaker (requires installation of `libsox-fmt-mp3`).  This requires setting the `AUDIODEV` to your speaker device.
  3) The third is to play an m3u playlist that points to the directory of kids songs.
  4) the fourth is a command kill music played with the second intent - this is called from Node-Red because the speakerphone cannot listen while playing music.
