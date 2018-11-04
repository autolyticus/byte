#!/usr/bin/env python2

import sys
import os
import datetime
sys.path.append('./kivymd')

from kivymd.theming import ThemeManager
from kivymd.selectioncontrols import MDCheckbox
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.material_resources import DEVICE_TYPE
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.label import MDLabel
from kivymd.dialog import MDDialog
from kivymd.date_picker import MDDatePicker
from kivymd.button import MDIconButton
from kivy.lang import Builder
from kivy.app import App

import subprocess, shlex
import sqlite3

# from kivy.metrics import dp
# from kivy.properties import ObjectProperty
# from kivy.uix.image import Image

# from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
# from kivymd.snackbar import Snackbar
# from plyer.facades import Orientation
# from kivymd.time_picker import MDTimePicker

from upload import TransferData


class SimpleApp(App):
    theme_cls = ThemeManager()
    theme_cls.theme_style = 'Dark'
    theme_cls.primary_palette = 'Indigo'

    def build(self, ):
        main_widget = Builder.load_file('./mdkvfile.kv')
        self.conn = sqlite3.connect('database.db')
        self.dpbox = TransferData()
        try:
            self.conn.execute(''' CREATE TABLE vox
                                (username text, timestamp text unique, data text);
                                ''')
        except:
            pass
        return main_widget

    def insertFile(self, fileData, username):
        query = '''INSERT INTO vox
                (username, timestamp, data) VALUES (?,?,?)'''
        cur =self.conn.cursor()
        cur.execute(query, (str(username), str(datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')), fileData))
        self.conn.commit()

    def send(self, fileName):
        # print(os.path.basename(fileName))
        return self.dpbox.upload_file(fileName, '/test_dropbox/' + os.path.basename(fileName))

    # def generateLink(self, fileName):
        # self.dpbox.


    def record(self, username):
        p = subprocess.Popen(shlex.split('python2 soundRecord.py %s' % username))
        p.wait()
        with open('output.wav') as f:
            a = f.read()
            self.insertFile(a, username)


if __name__ == '__main__':
    SimpleApp().run()
