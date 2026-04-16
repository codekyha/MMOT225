import time
import random
import os

# Ayarlari isletim sisteminden (Docker'dan) cekiyoruz
sensor_adi = os.getenv("SENSOR_ADI", "Varsayilan_Cihaz")
bekleme_suresi = int(os.getenv("BEKLEME", "3"))

print(f"--- {sensor_adi} Baslatildi. Her {bekleme_suresi} saniyede veri gonderecek ---", flush=True)

while True:
    sicaklik = random.uniform(20.0, 35.0)
    print(f"[{sensor_adi}] Anlik Sicaklik: {sicaklik:.2f} C", flush=True)
    time.sleep(bekleme_suresi)