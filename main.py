from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.network.urlrequest import UrlRequest
from kivy.utils import get_color_from_hex
import json

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class MacOranApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10,
