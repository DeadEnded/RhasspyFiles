# RhasspyFiles
misc. files for Rhasspy voice assistant.


## custom_handler.py
Custom intent handler for Rhasspy.

Currently setup with two intents:
  1) The first adjusted the speaker volume (change card to match your systems speaker device).
  2) The second is used to play local mp3 files through the speaker (requires installation of `libsox-fmt-mp3`).  This requires setting the `AUDIODEV` to your speaker device.
  
## songs.py
Songs slot program.

This scans the directory for files and generates a slot with the following design `songname:filepath`.

The song name has the directory and file extension stripped.  Underscores are also replaced with spaces to allow for voice recognition of the song name.
