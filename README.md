# arp-spoof-detector
Python ve Scapy kullanarak geliştirilmiş ağ güvenliği aracı: Gerçek zamanlı ARP Spoofing saldırılarını tespit eder.

## Takım Üyeleri
- Ferhat AKDEMİR

## Proje Açıklaması
**ARP Spoofing Tespit Aracı**, yerel ağlarda (LAN) gerçekleştirilen ARP Spoofing saldırılarını gerçek zamanlı olarak tespit etmek için Python ve Scapy kütüphanesi ile geliştirilmiştir. ARP Spoofing, bir saldırganın sahte ARP (Address Resolution Protocol - Adres Çözümleme Protokolü) yanıtları göndererek ağdaki cihazların MAC-IP eşleşmelerini manipüle ettiği bir Ortadaki Adam (Man-in-the-Middle - MitM) saldırı türüdür. Bu araç, ağdaki şüpheli ARP paketlerini izler, sahte yanıtları algılar ve kullanıcıyı uyarır.

Araç, modüler, genişletilebilir ve kullanıcı dostu bir yapıya sahiptir. Gerçek zamanlı tespit, otomatik ARP tablosu düzeltme, bildirim entegrasyonları ve görselleştirme gibi özelliklerle ağ yöneticileri ve güvenlik araştırmacıları için idealdir.

##  Hedefler
- **Gerçek Zamanlı Tespit:** ARP Spoofing saldırılarını anında algılama.
- **Kullanıcı Dostu Arayüz:** Komut satırı arayüzü (CLI) ile kolay kullanım, gelecekte GUI ve web arayüzü desteği.
- **Uyarı ve Loglama:** Şüpheli etkinlikleri bildirme ve detaylı log tutma.
- **Otomatik Düzeltme:** Zehirlenmiş ARP tablolarını otomatik olarak düzeltme.
- **Genişletilebilirlik:** DHCP veya DNS spoofing gibi diğer saldırı türlerini tespit etme desteği.

##  Özellikler
- **Gerçek Zamanlı ARP Paketi İzleme:** ARP yanıtlarını yakalar ve sahte yanıtları tespit eder.
- **Dinamik MAC-IP Eşleşme Tablosu:** Ağ taramasıyla meşru MAC-IP çiftlerini otomatik oluşturur ve günceller.
- **Otomatik ARP Tablosu Düzeltme:** Sahte ARP yanıtları tespit edildiğinde doğru yanıtlar gönderir.
- **Detaylı Loglama:** Şüpheli etkinlikleri zaman damgası, IP/MAC adresleri ve paket detaylarıyla kaydeder.
- **Bildirim Entegrasyonu:** E-posta veya anlık mesajlaşma (ör. Slack, Telegram) ile uyarı gönderimi.
- **Performans Optimizasyonu:** Çoklu iş parçacığı (threading) ile verimli paket izleme ve tarama.
- **Görselleştirme:** Tespit edilen saldırıların zaman bazlı grafiklerini oluşturma (Chart.js entegrasyonu).
- **Genişletilebilir Yapı:** DHCP veya DNS spoofing gibi ek saldırı türlerini tespit etme desteği.

##  Kullanılan Teknolojiler
- **Python 3.9+**: Aracın temel programlama dili.
- **Scapy**: Ağ paketi manipülasyonu ve analizi için kütüphane.
- **Chart.js** (isteğe bağlı): Saldırı trendlerini görselleştirmek için.
- **smtplib** (isteğe bağlı): E-posta bildirimleri için.

##  Kurulum
Aracı sisteminize kurmak için aşağıdaki adımları izleyin:

1. **Depoyu Klonlayın:**
   ```bash
   git clone https://github.com/Scofield1881/arp-spoof-detector.git
   cd arp-spoof-detector
   ```

2. **Gerekli Kütüphaneleri Kurun:**
   Python 3.9+ yüklü olduğundan emin olun, ardından gerekli kütüphaneleri kurun:
   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` içeriği:
   ```
   scapy
   ```

3. **Root Yetkileriyle Çalıştırın (Linux):**
   Paket izleme için root yetkileri gerekir:
   ```bash
   sudo python3 arp_detector.py [arayüz] [ip_aralığı]
   ```

##  Kullanım
Aracı varsayılan ağ arayüzü ve IP aralığı ile çalıştırabilir veya özel değerler belirtebilirsiniz:

```bash
sudo python3 arp_detector.py eth0 192.168.1.0/24
```

### Örnek Çıktı
```
ARP Spoofing Tespit Aracı Başlatılıyor...
Ağ tarandı, cihazlar: {'192.168.1.1': '00:1A:2B:3C:4D:5E', ...}
[2025-05-31 15:00:03] ARP Spoofing Tespit Edildi!
IP: 192.168.1.1, Şüpheli MAC: 00:XX:YY:ZZ:WW:VV, Beklenen MAC: 00:1A:2B:3C:4D:5E
ARP tablosu düzeltildi: 192.168.1.100
```

### Loglar
Loglar, proje dizinindeki `arp_spoof.log` dosyasına kaydedilir. Örnek log:
```
2025-05-31 15:00:03,123 - ARP Spoofing Tespit Edildi! IP: 192.168.1.1, Şüpheli MAC: 00:XX:YY:ZZ:WW:VV, Beklenen MAC: 00:1A:2B:3C:4D:5E
```

### Görselleştirme
Saldırı trendlerini görmek için web arayüzünü (eğer etkinleştirildiyse) çalıştırın:
```bash
python3 web_interface.py
```
Tarayıcıda `http://localhost:5000` adresine giderek tespit edilen saldırıların zaman bazlı grafiklerini görüntüleyin.

##  Nasıl Çalışır?
1. **Ağ Taraması:** ARP istekleriyle ağdaki ci,hazların MAC-IP eşleşmelerini tarar ve dinamik bir tablo oluşturur.
2. **Paket İzleme:** Scapy ile ARP yanıtları (`op=2`) yakalanır ve MAC-IP çiftleri bilinen tabloyla karşılaştırılır.
3. **Anomali Tespiti:** Bir IP adresi için beklenmeyen bir MAC adresi tespit edilirse, bu bir saldırı olarak işaretlenir.
4. **Uyarı ve Düzeltme:** Kullanıcı terminal, log veya bildirim yoluyla uyarılır; zehirlenmiş ARP tabloları doğru yanıtlarla düzeltilir.
5. **Periyodik Güncelleme:** Ağ, her 60 saniyede bir yeniden taranarak MAC-IP tablosu güncel tutulur.

##  Gelişmiş Yapılandırma
- **Özel Bildirim Ayarları:** E-posta veya mesajlaşma bildirimleri için `config.py` dosyasını düzenleyin (ör. Gmail SMTP, Telegram API).
- **Belirli IP Filtreleme:** `ip_range` parametresiyle belirli alt ağları izleyin.
- **Tarama Sıklığı:** `arp_detector.py` içindeki `time.sleep(60)` değerini değiştirerek tarama sıklığını ayarlayın.

##  Test Etme
Aracı test etmek için Scapy ile bir ARP Spoofing saldırısı simüle edin:
```python
from scapy.all import *
packet = ARP(op=2, pdst="192.168.1.100", psrc="192.168.1.1")
send(packet, iface="eth0")
```
Araç, sahte ARP yanıtını tespit etmeli ve bir uyarı loglamalıdır.

##  Planlanan Geliştirmeler
- **Grafiksel Arayüz (GUI):** Tkinter veya PyQt ile kullanıcı dostu bir arayüz ekleme.
- **Web Kontrol Paneli:** Flask tabanlı web arayüzünü geliştirerek gerçek zamanlı izleme ve görselleştirme.
- **DHCP/DNS Spoofing Tespiti:** Diğer ağ saldırılarını tespit etme desteği.
- **Güvenlik Duvarı Entegrasyonu:** Şüpheli MAC adreslerini otomatik engellemek için `iptables` kullanımı.
- **Makine Öğrenimi:** Yanlış pozitifleri azaltmak için anomali tespitinde ML kullanımı.

##  Katkıda Bulunma
Katkılarınızı bekliyoruz! Katkıda bulunmak için:
1. Depoyu forklayın.
2. Yeni bir dal oluşturun (`git checkout -b ozellik/yeni-ozellik`).
3. Değişikliklerinizi commit edin (`git commit -m "Yeni özellik eklendi"`).
4. Dalı itin (`git push origin ozellik/yeni-ozellik`).
5. Bir Pull Request açın.

Ayrıntılı rehber için `CONTRIBUTING.md` dosyasına bakın.

##  Yasal Uyarı
Bu araç **yalnızca eğitim ve etik amaçlarla** kullanılmalıdır. Sahip olmadığınız veya test etme izniniz olmayan sistemlerde ARP Spoofing veya ağ izleme yapmak yasa dışıdır ve ciddi hukuki sonuçlar doğurabilir. Her zaman açık izin alın.

##  Lisans
Bu proje MIT Lisansı ile lisanslanmıştır. Ayrıntılar için `LICENSE` dosyasına bakın.

##  İletişim
Sorularınız veya geri bildirimleriniz için Ferhat AKDEMİR ile ferhatakdemir870@gmail.com adresinden iletişime geçin veya GitHub'da bir issue açın.


## NOT
Bu proje temel düzeyde ARP spoofing tespiti sağlasa da, 2025 yılına yönelik gelişmiş uygulamalarda makine öğrenmesi ile desteklenen sistemler tercih edilmektedir. Projenin ileri versiyonlarında, Scapy ile toplanan veriler üzerinde davranışsal analiz yapılması ve ML modelleri ile dinamik tehdit algılama modülü geliştirilmesi planlanmaktadır.





