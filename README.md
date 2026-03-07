MMOT225: Bulut Bilişim - Hafta 5: Gelişmiş Docker Uygulamaları

Bu depo, MMOT225 Bulut Bilişim dersinin 5. haftasında işlenen Sanallaştırma, Hipervizör mimarileri ve Docker konteyner yönetimi konularına ait laboratuvar kılavuzunu ve teknik notları içermektedir.

Ders İçeriği ve Hedefler

Bu haftanın temel odak noktası, sanal makinelerin (VM) ötesine geçerek konteyner teknolojilerinin (Docker) bulut ekosistemindeki rolünü kavramak ve uygulamalı olarak bir Web sunucusu (Nginx) üzerinden kalıcı veri (Volumes) ve ağ yönetimi süreçlerini deneyimlemektir.

Teorik Kavramlar

Sanallaştırma Türleri: Type-1 (Bare Metal) ve Type-2 (Hosted) Hipervizör mimarileri.

Sanal Disk Yönetimi: * Thick Provisioning: Kapasitenin fiziksel diskten peşin ayrılması.

Thin Provisioning: Kapasitenin veri yazıldıkça dinamik olarak büyümesi.

Ağ Modelleri: NAT, Bridged ve Host-Only modlarının izolasyon ve erişilebilirlik farkları.

Konteynerizasyon: İşletim sistemi seviyesinde sanallaştırma ve Docker Engine mimarisi.

Laboratuvar Uygulaması: Adım Adım Docker Yönetimi

1. Sistem Hazırlığı ve Docker Kurulumu

Öncelikle Ubuntu Server sanal makineniz üzerinde paket listelerini güncelleyip Docker Engine kurulumunu gerçekleştirin:

# Paket listesini güncelle
sudo apt update

# Docker Engine kurulumu
sudo apt install docker.io -y

# Servisi etkinleştir ve başlat
sudo systemctl enable --now docker


2. Nginx Web Sunucusu ve Port Yönlendirme

İzole bir konteyner içinde çalışan Nginx sunucusunu, ana makinenin (Host) $8080$ portuna bağlayarak çalıştırın:

sudo docker run -d -p 8080:80 --name benim-sitem nginx


3. Konteyner İçine Erişim ve Log Yönetimi

Çalışan bir konteynerin içindeki dosya sistemine erişmek ve arka plan kayıtlarını incelemek için aşağıdaki komutları kullanın:

Log İzleme: sudo docker logs benim-sitem

İnteraktif Shell Erişimi: sudo docker exec -it benim-sitem bash

4. Kalıcı Veri Yönetimi (Volumes / Bind Mounts)

Konteynerler silindiğinde verilerin kaybolmaması için yerel bir dizini konteynere bağlayın. Bu yöntemle kendi HTML dosyanızı yayınlayabilirsiniz:

# Yerel dizin hazırlığı
mkdir ~/sitem
echo "<h1>MMOT225 Bulut Bilisim Laboratuvari</h1>" > ~/sitem/index.html

# Klasörü bağlayarak konteyneri başlatma
sudo docker run -d -p 8080:80 -v ~/sitem:/usr/share/nginx/html --name benim-sitem nginx


Ağ Yapılandırması ve Erişim

Sanal makine içindeki uygulamaya fiziksel ana makinenizden erişmek için sanal makinenin IP adresini öğrenmeniz gerekmektedir:

ip a
# veya
hostname -I


Erişim Protokolü: Tarayıcı adres çubuğuna: http://<VM_IP_ADRESI>:8080

Not: Fiziksel makineden erişim sağlanamıyorsa, sanal makinenin ağ ayarlarının Bridged Adapter veya Host-Only olarak yapılandırıldığından emin olun.

Önemli Docker Komutları (Hızlı Referans)

Komut

Açıklama

docker ps

Çalışan konteynerleri listeler

docker ps -a

Durmuş olanlar dahil tüm konteynerleri listeler

docker images

Yerel imajları listeler

docker stop <ID>

Belirtilen konteyneri durdurur

docker rm <ID>

Belirtilen konteyneri siler

docker logs <ID>

Konteyner çıktılarını gösterir

Teslim Edilecekler

Laboratuvar çalışması sonunda aşağıdaki çıktıları hazırlayınız:

Konteyner içinde bash oturumuna ait terminal görüntüsü.

Fiziksel makine tarayıcısından erişilen özel HTML sayfasının ekran görüntüsü.

-v parametresinin uygulama geliştirme döngüsündeki avantajlarını açıklayan kısa rapor.

Eğitmen: Dr. Öğr. Üyesi Hasan Oğuz

Kurum: İstanbul Okan Üniversitesi - Meslek Yüksekokulu
