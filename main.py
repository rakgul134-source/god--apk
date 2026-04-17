from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)

class TanriApp(App):
    def build(self):
        layout = BoxLayout(padding=50)
        
        btn = Button(
            text='ÇALIŞIYOR KRAL\nBANA TIKLA', 
            font_size='30sp',
            background_color=(0, 1, 0, 1)
        )
        
        def tiklandi(instance):
            instance.text = 'HELAL BAŞKAN\nBASTIN BANA'
        
        btn.bind(on_press=tiklandi)
        layout.add_widget(btn)
        return layout

TanriApp().run()
