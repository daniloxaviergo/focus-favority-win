#!/usr/bin/python

import gi
import os
import sys
import re
import json

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

outt = os.popen('/home/danilo/scripts/get_current_window.sh').read()
current_window_id = outt.replace(',', '').split('x')[1]
current_window_id = re.sub(r'(\r\n\t|\n|\r\t|\n)', '', current_window_id)

outt = os.popen('wmctrl -dliGu').read()
lines = outt.split("\n")
wmctrl_line = ''

for line in lines:
  if line.find(current_window_id) >= 0:
    wmctrl_line = line

class SaveWindowId(Gtk.Window):
  def __init__(self):
    Gtk.Window.__init__(self, title="save window id", default_width=500, default_height=230)
    self.border_width = 10

    self.connect("key-press-event", self.on_window_key_press)

    self.box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    self.add(self.box_outer)

    self.listbox = Gtk.ListBox()
    self.listbox.selection_mode = Gtk.SelectionMode.NONE
    self.box_outer.pack_start(self.listbox, True, True, 0)

    self.row = Gtk.ListBoxRow()
    self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
    self.row.add(self.hbox)
    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.hbox.pack_start(self.vbox, True, True, 0)

    self.label1 = Gtk.Label(label=wmctrl_line, xalign=0, ellipsize=True)
    self.vbox.pack_start(self.label1, True, True, 0);

    self.listbox.add(self.row)

    self.row = Gtk.ListBoxRow()
    self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
    self.row.add(self.hbox)
    self.label = Gtk.Label(label="Atalho", xalign=0)
    self.combo = Gtk.ComboBoxText()
    self.combo.insert(0,  "0",  "s1")
    self.combo.insert(1,  "1",  "s2")
    self.combo.insert(2,  "2",  "s3")
    self.combo.insert(3,  "3",  "s4")
    self.combo.insert(4,  "4",  "s5")
    self.combo.insert(5,  "5",  "s6")
    self.combo.insert(6,  "6",  "s7")
    self.combo.insert(7,  "7",  "s8")
    self.combo.insert(8,  "8",  "s9")
    self.combo.insert(9,  "9",  "ss1")
    self.combo.insert(10, "10", "ss2")
    self.combo.insert(11, "11", "ss3")
    self.combo.insert(12, "12", "ss4")
    self.combo.insert(13, "13", "ss5")
    self.combo.insert(14, "14", "ss6")
    self.combo.insert(15, "15", "ss7")
    self.combo.insert(16, "16", "ss8")
    self.combo.insert(17, "17", "ss9")
    self.hbox.pack_start(self.label, False, True, 0)
    self.hbox.pack_start(self.combo, True, True, 0)

    self.vbox.pack_start(self.row, True, True, 0)

    self.button = Gtk.Button(label="Save")
    self.button.connect("clicked", self.on_button_clicked)
    self.vbox.pack_start(self.button, True, True, 0)

  def on_window_key_press(self, widget, event):
    keycode = event.get_keycode()[1]

    if(keycode == 9):
      sys.exit()

  def on_button_clicked(self, widget):
    if self.combo.get_active_text() == None:
      return

    str_json = open("/home/danilo/scripts/wids.json", "r").read()
    jjson = json.loads(str_json)

    key_json = self.combo.get_active_text()
    jjson[key_json] = wmctrl_line

    wids = open("/home/danilo/scripts/wids.json", "w")
    wids.write(json.dumps(jjson))
    wids.close()

    sys.exit()

win = SaveWindowId()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
