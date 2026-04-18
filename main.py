from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class AvciAvApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.oran_input = TextInput(
            hint_text='Oran gir: 4.31',
            multiline=False,
            input_filter='float',
            font_size=32,
            size_hint_y=0.2
        )
        
        self.hesapla_btn = Button(
            text='HESAPLA',
            font_size=28,
            size_hint_y=0.2,
            on_pressAVCI, build patlamış. O yüzden **indirme kısmı yok**. APK oluşmadı.

**Sebep**: `Build APK and Accept Licenses` adımında kırmızı X var. 13dk 56sn’de çakılmış.

### Bu hatanın %99 sebebi `main.py` yarım kaldı
Bir önceki attığın fotoda `main.py` kodu `font|` satırında bitiyordu. Yarım kalan Python dosyasını buildozer derleyemez, direkt hata verir.

### Şimdi 2 adımda çözüyoruz:

**1. Hatayı görmek için**  
Ekrandaki `Build APK and Accept Licenses` yazısına tıkla. En altta `SyntaxError` veya `IndentationError` yazar. O da zaten "dosya yarım" diyecek.

**2. Çözmek
