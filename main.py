from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1) # Koyu arka plan

class AvciAvApp(App):
    def build(self):
        self.title = "AVCI 01 1 0"

        # Ana düzen
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Başlık
        baslik = Label(
            text='[b]AVCI[/b] 01 1 0 KURALI',
            markup=True,
            font_size='24sp',
            size_hint_y=0.2,
            color=(1, 0.8, 0, 1)
        )

        # Giriş kutusu
        self.oran_input = TextInput(
            hint_text='Oranı gir: 4.31',
            multiline=False,
            input_filter='float',
            font_size='22sp',
            size_hint_y=0.15,
            halign='center',
            padding_y=[15, 15]
        )

        # Buton
        hesapla_btn = Button(
            text='SORGULA',
            font_size='20sp',
            size_hint_y=0.15,
            background_color=(0.2, 0.6, 1),
            on_pressHaklısın AVCI 👑 Sürekli "Something went wrong" gelmesi sinir bozucu. Benim tarafımda bir hata oldu, sende sorun yok.

**ÖNCE BU SORUNU ÇÖZELİM: main.py dosyan yarım kalmış**

Senin ekran görüntündeki kod `font|` satırında kesilmiş. O yüzden APK boş çıkıyor.

### 1. main.py'yi tamamen sil, bunu yapıştır:

```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window

Window.clearcolor = (0.1, 0.1, 0.1, 1) # Koyu tema

class AvciAvApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)

        self.baslik = Label(
            text='AVCI AV HESAPLAYICI 👑\
