#!/usr/bin/env python

import sys
import json
import subprocess

def speech(text):
    global o
    o["speech"] = {"text": text}

# get json from stdin and load into python dict
o = json.loads(sys.stdin.read())

intent = o["intent"]["name"]
volume = o.get("slots").get("volume")
song = o.get("slots").get("song")

if intent == "AdjustVolume":
    subprocess.call("amixer -c 1 set 'PCM',0 {}% > /dev/null 2>&1".format(volume),shell=True)
    speech("Volume set to {} percent".format(volume))

elif intent == "PlaySong":
    subprocess.call("play -q {} > /dev/null 2>&1".format(song),shell=True, env={"AUDIODEV":"hw:1,0"})

# convert dict to json and print to stdout
print(json.dumps(o))
