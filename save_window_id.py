#!/usr/bin/python

import gi
import os
import sys
import re
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

sys.path.append("/home/danilo/scripts/")

from wmctrl_window import WmctrlWindow

def get_current_window():
  outt = os.popen('/home/danilo/scripts/get_current_window.sh').read()
  current_window_id = outt.replace(',', '').split('x')[1]
  current_window_id = re.sub(r'(\r\n\t|\n|\r\t|\n)', '', current_window_id)

  outt = os.popen('wmctrl -dliGu').read()
  lines = outt.split("\n")
  wmctrl_line = ''

  for line in lines:
    if line.find(current_window_id) >= 0:
      wmctrl_line = line
  return wmctrl_line

class SaveWindowId:
  def on_window1_destroy(self, *args):
    Gtk.main_quit()

  def on_window1_show(self, window1):
    label1 = builder.get_object('label1')
    combo = builder.get_object('combo')
    active_window = WmctrlWindow(wmctrl_line)

    label1.set_text(active_window.kname)
    combo.insert(0,  '0',  's1')
    combo.insert(1,  '1',  's2')
    combo.insert(2,  '2',  's3')
    combo.insert(3,  '3',  's4')
    combo.insert(4,  '4',  's5')
    combo.insert(5,  '5',  's6')
    combo.insert(6,  '6',  's7')
    combo.insert(7,  '7',  's8')
    combo.insert(8,  '8',  's9')
    combo.insert(9,  '9',  'ss1')
    combo.insert(10, '10', 'ss2')
    combo.insert(11, '11', 'ss3')
    combo.insert(12, '12', 'ss4')
    combo.insert(13, '13', 'ss5')
    combo.insert(14, '14', 'ss6')
    combo.insert(15, '15', 'ss7')
    combo.insert(16, '16', 'ss8')
    combo.insert(17, '17', 'ss9')
    combo.insert(18, '18', 'alt1')
    combo.insert(19, '19', 'alt2')
    combo.insert(20, '20', 'alt3')
    combo.insert(21, '21', 'alt4')
    combo.insert(22, '22', 'alt5')
    combo.insert(23, '23', 'alt6')
    combo.insert(24, '24', 'alt7')
    combo.insert(25, '25', 'alt8')
    combo.insert(26, '26', 'alt9')

  def on_window1_key_press_event(self, window, event):
    keycode = event.get_keycode()[1]

    if(keycode == 9):
      sys.exit()

  def on_button_clicked(self, button):
    combo = builder.get_object('combo')
    label1 = builder.get_object('label1')

    if combo.get_active_text() == None:
      return

    str_json = open('/home/danilo/scripts/wids.json', 'r').read()
    jjson = json.loads(str_json)

    key_json = combo.get_active_text()
    jjson[key_json] = wmctrl_line

    wids = open('/home/danilo/scripts/wids.json', 'w')
    wids.write(json.dumps(jjson))
    wids.close()

    sys.exit()

wmctrl_line = get_current_window()
builder = Gtk.Builder()
builder.add_from_file('/home/danilo/scripts/save_window_id.glade')
builder.connect_signals(SaveWindowId())

window = builder.get_object('window1')
window.show_all()

Gtk.main()
