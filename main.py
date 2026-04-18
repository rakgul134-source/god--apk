from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class AvciAvApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.baslik = Label(
            text='AVCI AV - 01 1 0 Kuralı',
            font_size='24sp',
            size_hint_y=None,
            height=50
