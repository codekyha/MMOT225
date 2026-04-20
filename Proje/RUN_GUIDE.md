# 🚀 Mini Kod Çalıştırma El Kitapçığı

Bu kitapçık, proje kapsamında geliştirilen Python uygulamalarının ve Docker konteynerlerinin yerel ortamda nasıl derlenip çalıştırılacağına dair hızlı komut referanslarını içerir.

## 1. Standart Python Betiği Çalıştırma (Geliştirme Aşaması)

Kodu Docker'a almadan önce yerel makinenizde test etmek için terminal veya komut satırını kullanabilirsiniz.

**Gereksinimlerin Yüklenmesi:**
Eğer projenizde dışa bağımlı kütüphaneler (örneğin Flask) varsa, sanal ortamda kurulum yapmanız önerilir:

```bash
pip install flask
```

**Kodu Çalıştırma:**

```bash
python app.py
# macOS veya Linux (Pardus/Ubuntu) ortamlarında alternatif olarak:
python3 app.py
```

*Uygulama varsayılan olarak `http://127.0.0.1:5000` adresinde ayağa kalkacaktır.*

## 2. Docker ile İzole Ortamda Çalıştırma (Dağıtım Aşaması)

Uygulamayı çoklu müşteri (multi-tenant) mimarisinde çalıştırmak için Docker imajları ve konteynerleri kullanılır. İşlemler sırasıyla `Dockerfile` ve `app.py` dosyalarının bulunduğu dizinde yapılmalıdır.

### Adım 2.1: İmaj Derleme (Build)

Uygulamanızı ve gerekli bağımlılıkları içeren kalıp (imaj) dosyasını oluşturun:

```bash
docker build -t bulut-projesi .
```

*(Sonundaki nokta (`.`) komutun bulunduğu dizindeki Dockerfile'ı işaret eder.)*

### Adım 2.2: Konteynerleri Ayağa Kaldırma (Run & Port Yönlendirme)

Aynı imajı kullanarak farklı portlarda izole konteynerler başlatabilirsiniz:

```bash
# Birinci müşteri için (Host 8081 portundan 5000'e yönlendirme)
docker run -d -p 8081:5000 --name musteri_A bulut-projesi

# İkinci müşteri için (Host 8082 portundan 5000'e yönlendirme)
docker run -d -p 8082:5000 --name musteri_B bulut-projesi
```

## 3. Ortam Değişkenleri (ENV) ile Dinamik Çalıştırma

Kodun içini değiştirmeden, konteyner ayağa kalkarken dışarıdan parametre (`-e`) göndermek sanallaştırmanın temelidir.

**Parametrik Çalıştırma Örneği:**

```bash
docker run -d -p 8083:5000 \
  -e MUSTERI_ADI="Firma C" \
  -e HIZMET_SEVIYESI="Premium" \
  -e TEMA_RENGI="#FF5733" \
  --name musteri_C bulut-projesi
```

## 4. Sistem Kontrolü ve Sorun Giderme

Sistemde neler olup bittiğini anlamak için aşağıdaki izleme komutlarını kullanabilirsiniz.

**Aktif Konteynerleri Listeleme:**
Şu anda çalışan tüm konteynerleri, port yönlendirmelerini ve ID numaralarını görmek için:

```bash
docker ps
```

**Uygulama Hatalarını (Logları) Okuma:**
Eğer bir konteyner çalışıyor ama tarayıcıda sayfa açılmıyorsa, uygulamanın içindeki logları okuyun:

```bash
docker logs musteri_A
```

**Konteyneri Durdurma ve Silme:**
Test işlemleriniz bittiğinde veya port çakışması yaşadığınızda mevcut konteyneri kapatabilirsiniz:

```bash
docker stop musteri_A
docker rm musteri_A
```
