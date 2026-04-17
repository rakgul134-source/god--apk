from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class TanriApp(App):
    def tiklandi(self, instance):
        popup = Popup(title='TANRI APK',
                      content=Label(text='ÇALIŞIYOR KRAL!'),
                      size_hint=(0.6, 0.4))
        popup.open()
