#!/usr/bin/python

import os
import sys
import json
import re

str_json = open("/home/danilo/scripts/wids.json", "r").read()
jjson = json.loads(str_json)

key_json = sys.argv[1]
line = jjson[key_json]

# first_part = line.split('xavier')[0]
attrs = re.findall(r'[^\s]+', line)

win_id = attrs[0]
workspace = attrs[1]

current_workspace = os.popen("wmctrl -d | grep '*' | cut -d ' ' -f1").read()
current_workspace = re.sub(r'(\r\n\t|\n|\r\t|\n)', '', current_workspace)

if current_workspace != workspace:
  os.popen("xdotool set_desktop {work}".format(work=workspace)).read()

os.popen('wmctrl -i -a {win_id}'.format(win_id=win_id)).read()
sys.exit()
