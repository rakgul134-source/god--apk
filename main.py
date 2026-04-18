from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AvciAvApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.oran_input = TextInput(
            hint_text='Oran gir: 4.31',
            multiline=False,
            input_filter='float',
            font
