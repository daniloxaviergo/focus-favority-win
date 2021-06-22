#!/usr/bin/python3

import gi
import os
import sys
import re
import json
import dmenu
import time

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

sys.path.append("/home/danilo/scripts/")
from wmctrl_window import WmctrlWindow

str_json = open("/home/danilo/scripts/tilix_mapping.json", "r").read()
tilix_mapping = json.loads(str_json)
list_to_show = []

for name in tilix_mapping.keys():
  list_to_show.append(name)

option = dmenu.show(list_to_show, case_insensitive=True, lines=20, bottom=True, monitor=3, font='Monospace-16:normal')
item = tilix_mapping.get(option, None)

if not item:
  sys.exit()

# {"dxfac": {"session": "4", "tag": "1", "window": "0x06401143  1 7680 1350 2880 1620 xavier s6"}}

window = WmctrlWindow(item['window'])
window.set_focus()
time.sleep(0.2)

session = int(item.get('session', 0))
tab = int(item.get('tab', 0))
init_text = item.get('init_text', None)

if session > 0:
  os.popen(f'xdotool key ctrl+alt+{session}').read()

if tab > 0:
  os.popen(f'xdotool key super+shift+Up').read()
  os.popen(f'xdotool key super+shift+Left').read()

  if tab == 2:
    os.popen(f'xdotool key super+shift+Right').read()

  if tab == 3:
    os.popen(f'xdotool key super+shift+Down').read()

  if tab == 4:
    os.popen(f'xdotool key super+shift+Right').read()
    os.popen(f'xdotool key super+shift+Down').read()

if init_text:
  os.popen(f"xdotool type '{init_text}'").read()
