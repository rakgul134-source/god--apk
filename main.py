from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock
import requests

Window.clearcolor = (0.05, 0.05, 0.05, 1)

class OranApp(App):
    def build(self):
        ana_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
