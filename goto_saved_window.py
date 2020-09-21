#!/usr/bin/python

import os
import sys
import json
import re

str_json = open("/home/danilo/scripts/wids.json", "r").read()
jjson = json.loads(str_json)

key_json = sys.argv[1]
line = jjson[key_json]
by_class_name = line[0] != '0'

if by_class_name:
  os.popen('/home/danilo/scripts/dmenu/focus_class_name.py {class_window}'.format(class_window=line)).read()
  sys.exit()

first_part = line.split('xavier')[0]
attrs = re.findall(r'[^\s]+', first_part)

win_id = attrs[0]
workspace = attrs[1]

current_workspace = os.popen("wmctrl -d | grep '*' | cut -d ' ' -f1").read()
current_workspace = re.sub(r'(\r\n\t|\n|\r\t|\n)', '', current_workspace)
common_behavior   = key_json[:3] != 'alt'

window_exists = len(os.popen("wmctrl -dliGux | grep {win_id}".format(win_id=win_id)).read()) > 0
if not window_exists:
  sys.exit()

if current_workspace != workspace and common_behavior:
  os.popen("xdotool set_desktop {work}".format(work=workspace)).read()

if not common_behavior:
  os.popen('wmctrl -r -R -i -a {win_id} -t {work}'.format(win_id=win_id, work=current_workspace)).read()

  # if focus windows minimize
  active_window = os.popen('printf 0x%x "$(xdotool getwindowfocus)"').read()
  if int(active_window, 16) == int(win_id, 16):
    os.popen('xdotool getactivewindow windowminimize').read()
    sys.exit()

os.popen('wmctrl -i -a {win_id}'.format(win_id=win_id)).read()
sys.exit()
