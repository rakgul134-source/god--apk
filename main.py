from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import calendar
from datetime import datetime

class TakvimApp(App):
    def build(self):
        self.bu_ay = datetime.now().month
        self.bu_yil = datetime.now().year
        
        self.ana_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        ust_bar = BoxLayout(size_hint_y=0.15, spacing=10)
        
        geri_btn = Button(text='<', font_size='25sp', on_pressTamam kanka, en basiti. Ne maç ne internet. Sadece açılsın, ekranda takvim gibi bir şey göstersin. Çökme ihtimali sıfır.

### 1. `buildozer.spec`
Bunu kullan. `requests` falan yok:
