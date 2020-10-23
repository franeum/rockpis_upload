#!/usr/bin/env python3

import kivy 
  
# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App 
from kivy.uix.spinner import Spinner
  
# this restrict the kivy version i.e 
# below this kivy version you cannot  
# use the app or software 
# not coumpulsary to write it 
kivy.require('1.9.1') 
  
# define the App class 
# and just pass rest write on kvfile 
# not necessary to pass 
# can also define function in it 
class kvfileApp(App): 
    pass
  
kv = kvfileApp() 
kv.run() 