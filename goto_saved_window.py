#!/usr/bin/python

import os
import sys
import json
import re

str_json = open("/home/danilo/scripts/wids.json", "r").read()
jjson = json.loads(str_json)

key_json = sys.argv[1]
line = jjson[key_json]

first_part = line.split('xavier')[0]
attrs = re.findall(r'[^\s]+', first_part)

win_id = attrs[0]
workspace = attrs[1]

current_workspace = os.popen("wmctrl -d | grep '*' | cut -d ' ' -f1").read()
current_workspace = re.sub(r'(\r\n\t|\n|\r\t|\n)', '', current_workspace)
change_workspace  = key_json[:3] != 'alt'

if current_workspace != workspace and change_workspace:
  os.popen("xdotool set_desktop {work}".format(work=workspace)).read()

if not change_workspace:
  os.popen('wmctrl -r -R -i -a {win_id} -t {work}'.format(win_id=win_id, work=current_workspace)).read()

os.popen('wmctrl -i -a {win_id}'.format(win_id=win_id)).read()
sys.exit()
