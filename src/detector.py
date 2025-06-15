from scapy.all import ARP, sniff
from datetime import datetime

# IP-MAC eşleşmelerini tutan sözlük
ip_mac_table = {
    "192.168.1.1": "ec:be:5f:c7:85:fd",  # Gerçek modem MAC’i
    "192.168.1.200": "c0:a5:e8:56:18:87" # Senin bilgisayarın MAC’i
}


# Her yakalanan ARP paketini işleyen fonksiyon
def detect_arp_spoof(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        ip = packet[ARP].psrc   # Paketin belirttiği IP adresi
        mac = packet[ARP].hwsrc # Paketin belirttiği MAC adresi

        if ip in ip_mac_table:
            if ip_mac_table[ip] != mac:
                alert_msg = f"[⚠️ ALERT] ARP Spoofing Detected! IP: {ip} was {ip_mac_table[ip]}, now {mac}"
                print(alert_msg)

                # log.txt dosyasına yaz (isteğe bağlı loglama)
                with open("alerts.txt", "a") as f:
                    f.write(f"{datetime.now()} - {alert_msg}\n")
            else:
                print(f"[✓] IP {ip} yine aynı MAC ile geldi: {mac}")
        else:
            ip_mac_table[ip] = mac
            print(f"[+] İlk kez görülen IP {ip}, MAC olarak {mac} kaydedildi.")

# Ana döngü - sürekli ARP paketlerini dinle
print("[*] Monitoring ARP packets for spoofing...")
sniff(filter="arp", prn=detect_arp_spoof, store=0)
