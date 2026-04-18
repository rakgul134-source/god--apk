
### 2. `main.py` - komple sil bunu yapıştır
```python
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime

class TakvimApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50)
        
        tarih = datetime.now().strftime("%d.%m.%Y")
        saat = datetime.now().strftime("%H:%M:%S")
        
        baslik = Label(
            text='BASIT TAKVIM',
            font_size='30sp',
            size_hint_y=0.2,
            bold=True
        )
        
        tarih_label = Label(
            text=f'Bugun: {tarih}',
            font_size='24sp',
            size_hint_y=0.2
        )
        
        saat_label = Label(
            text=f'Saat: {saat}',
            font_size='24sp',
            size_hint_y=0.2
        )
        
        bilgi = Label(
            text='Uygulama calisiyor.',
            font_size='18sp',
            size_hint_y=0.4
        )
        
        layout.add_widget(baslik)
        layout.add_widget(tarih_label)
        layout.add_widget(saat_label)
        layout.add_widget(bilgi)
        
        return layout

TakvimApp().run()
