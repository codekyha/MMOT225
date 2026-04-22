from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

# Ortam değişkenlerini (ENV) alıyoruz
musteri_adi = os.getenv(MUSTERI_ADI, Misafir Kurum)
tema_rengi = os.getenv(TEMA_RENGI, #333333)
hizmet_seviyesi = os.getenv(HIZMET_SEVIYESI, Standart)

# Dinamik Tema Rengi İçeren Temel HTML Şablonu 
html_sablon = 
!DOCTYPE html
html
head
    titleSaaS Kontrol Panelititle
head
body style=font-family Arial, sans-serif; padding 30px; color {renk}; background-color #f9f9f9;
    div style=border 2px solid {renk}; padding 20px; border-radius 10px; background-color white;
        h2Bulut Hizmetleri Kontrol Panelih2
        hr style=border-color {renk};
        {icerik}
    div
body
html


# Route 1 Ana Sayfa 
@app.route('')
def ana_sayfa()
    icerik = f
    h1Hoş Geldiniz, {musteri_adi}h1
    pAktif Hizmet Seviyeniz strong{hizmet_seviyesi}strongp
    pBu alan firmanıza özel izole edilmiş bir Docker konteyneri üzerinde çalışmaktadır.p
    
    return html_sablon.format(renk=tema_rengi, icerik=icerik)

# Route 2 Sistem Raporu 
@app.route('rapor')
def sistem_raporu()
    zaman = datetime.now().strftime(%Y-%m-%d %H%M%S)
    icerik = f
    h3Anlık Sistem Raporuh3
    ul
        listrongFirmaMüşteristrong {musteri_adi}li
        listrongSunucu Saatistrong {zaman}li
        listrongSistem Durumustrong Çevrimiçi ve Stabilli
    ul
    
    return html_sablon.format(renk=tema_rengi, icerik=icerik)

# Route 3 Destek Talebi 
@app.route('destek')
def destek_talebi()
    icerik = f
    h3Destek ve İletişim Merkezih3
    pSayın strong{musteri_adi}strong yetkilisi, em{hizmet_seviyesi}em paket müşterimiz olduğunuz için talepleriniz bu seviyeye göre önceliklendirilecektir.p
    pLütfen sistem yöneticiniz ile iletişime geçiniz.p
    
    return html_sablon.format(renk=tema_rengi, icerik=icerik)

if __name__ == '__main__'
    # Flask uygulamasının dışarıdan erişilebilir olması için host='0.0.0.0' [cite 170]
    app.run(host='0.0.0.0', port=5000)