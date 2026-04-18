from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = (0.1, 0.1, 0.1, 1)

class AvciAvApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.baslik = Label(
            text='AVCI AV 01 1 0 KURALI',
            font_size='24sp',
            size_hint_y=0.2,
            color=get_color_from_hex('#00FF00')
        )
        
        self.input = TextInput(
            hint_text='Ondalikli sayi gir: 2.05',
