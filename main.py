import itertools

# HEDEF ORANLAR - İblis'in kutsal sayıları
HEDEF_ORANLAR = [3.11, 3.20, 4.30]
TOLERANS = 0.005 # 3.105 - 3.115 arası kabul

def oran_yakala(orant):
    """3.11, 3.20, 4.30 yakalandı mı kontrol"""
    for hedef in HEDEF_ORANLAR:
        if abs(orant - hedef) <= TOLERANS:
            return hedef
    return None

def predator_tara(mac_adi, oranlar_dict):
    """
    oranlar_dict formatı:
    {
        "MS_1": 2.40,
        "MS_X": 3.11,
        "MS_2": 3.00,
        "IY_1": 3.20,
        "IY_X": 2.10,
        "IY_2": 3.50,
        "ALT": 1.85,
        "UST": 1.95,
        "KG_VAR": 1.80,
        "KG_YOK": 2.00
    }
    """
    bulunan_avlar = []

    # 1. TEKLİ ORANLAR - Direkt 3.11/3.20/4.30 var mı?
    for market, oran in oranlar_dict.items():
        yakalanan = oran_yakala(oran)
        if yakalanan:
            bulunan_avlar.append({
                "tip": "TEKLI",
                "kombinasyon": market,
                "oran": oran,
                "hedef": yakalanan
            })

    # 2. İKİLİ KOMBİNASYONLAR - Çarpım 3.11/3.20/4.30 yapıyor mu?
    marketler = list(oranlar_dict.keys())
    for kombo in itertools.combinations(marketler, 2):
        # Aynı market tipini kombine etme: MS_1 + MS_X olmaz
        if kombo[0].split('_')[0] == kombo[1].split('_')[0]:
            continue

        oran1, oran2 = oranlar_dict[kombo[0]], oranlar_dict[kombo[1]]
        carpan = round(oran1 * oran2, 3)
        yakalanan = oran_yakala(carpan)

        if yakalanan:
            bulunan_avlar.append({
                "tip": "IKILI",
                "kombinasyon": f"{kombo[0]} x {kombo[1]}",
                "oran": carpan,
                "hedef": yakalanan
            })

    # 3. SONUCU BAS
    print(f"\n🔥 PREDATÖR RAPORU: {mac_adi} 22:45 🔥")
    if bulunan_avlar:
        for av in bulunan_avlar:
            print(f"✅ AV BULUNDU | {av['tip']} | {av['kombinasyon']} = {av['oran']} → HEDEF {av['hedef']}")
    else:
        print("❌ Bu maçta 3.11 / 3.20 / 4.30 avı yok. Geç.")

    return bulunan_avlar

# RIO AVE - AVS TEST VERİSİ - Sen gerçek oranları girersin
rio_ave_oranlar = {
    "MS_1": 2.35,
    "MS_X": 3.11, # BAK AV!
    "MS_2": 3.10,
    "IY_1": 2.95,
    "IY_X": 2.05,
    "IY_2": 3.20, # BAK AV!
    "ALT_25": 1.88,
    "UST_25": 1.92,
    "KG_VAR": 1.78,
    "KG_YOK": 2.02
}

# ÇALIŞTIR
predator_tara("Rio Ave - AVS", rio_ave_oranlar)
