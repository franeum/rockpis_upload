#!/usr/bin/env python3

import conn 
import kivy 
  
# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
  
# this restrict the kivy version i.e 
# below this kivy version you cannot  
# use the app or software 
# not coumpulsary to write it 
kivy.require('1.11.1') 
  

class MainBox(BoxLayout): 
    # For Spinner defining spinner clicked function 
    def spinner_clicked(self, value): 
        print("Language selected is " + value) 

class MyLabel(Label):
    def format_text(self, txt):
        return '[color=#88e5af][b]' + txt + '[/b][/color]'

# define the App class 
# and just pass rest write on kvfile 
# not necessary to pass 
# can also define function in it 
class kvfileApp(App): 
    networks = conn.enumerate_wifi(conn.get_available_wifi()) 
    networks = [x[1] for x in networks]
    def build(self):
        return MainBox()

  
kv = kvfileApp() 
kv.run() 