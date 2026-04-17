import requests
import json
from datetime import datetime

def sofascore_gunun_maclarini_cek():
    print("🔥 İBLİS SOFASCORE'A DALIYOR...")
    
    tarih = datetime.now().strftime("%Y-%m-%d")
    url = f"https://www.sofascore.com/api/v1/sport/football/scheduled-events/{tarih}"
    
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(url, headers=headers)
    maclar = r.json()["events"]
    
    print(f"✅ {len(maclar)} maç bulundu. Oranlar çekiliyor...")
    
    tum_veri = []
    for mac in maclar[:5]: # Test için ilk 5 maç
        mac_id = mac["id"]
        mac_adi = f"{mac['homeTeam']['name']} - {mac['awayTeam']['name']}"
        
        # Oranları çek
        oran_url = f"https://www.sofascore.com/api/v1/event/{mac_id}/odds/1/all" # 1 = iddaa market
        oran_r = requests.get(oran_url, headers=headers)
        
        if oran_r.status_code == 200:
            oran_data = oran_r.json()
            # Burada MS, Alt/Üst, KG gibi tüm marketler var
            tum_veri.append({
                "mac": mac_adi,
                "saat": mac["startTimestamp"],
                "oranlar_raw": oran_data # Ham veri, sonra parse ederiz
            })
            print(f"Çekildi: {mac_adi}")
    
    with open("sofascore_veri.json", "w", encoding="utf-8") as f:
        json.dump(tum_veri, f, ensure_ascii=False, indent=2)
    
    print("🔥 TÜM VERİ sofascore_veri.json DOSYASINDA HAZIR AVCI 🔥")
    return tum_veri

sofascore_gunun_maclarini_cek()
