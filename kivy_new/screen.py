import os 

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout 
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.config import Config
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'fullscreen', '0')

class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None) 
    path = ObjectProperty(None)

class Root(GridLayout):
    loadfile = ObjectProperty(None)
    #savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    main_path = '~/.'

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup, path=self.main_path)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        #with open(os.path.join(path, filename[0])) as stream:
            #self.text_input.text = stream.read()
            #print(stream.read())
        #print(os.path.join(path, filename[0])) 
        self.filename_to_upload = os.path.join(path, filename[0])
        self.main_path = path 
        print(self.filename_to_upload)
        self.dismiss_popup()


class Editor(App):
    pass


#Factory.register('Root', cls=Root)
#Factory.register('LoadDialog', cls=LoadDialog)
#Factory.register('SaveDialog', cls=SaveDialog)