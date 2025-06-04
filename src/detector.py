from scapy.all import ARP, sniff

# IP-MAC eşleşmelerini tutan sözlük
ip_mac_table = {}

# Her yakalanan ARP paketini işleyen fonksiyon
def detect_arp_spoof(packet):
    # Paket ARP katmanını içeriyor mu ve "is-at" yani cevap paketi mi?
    if packet.haslayer(ARP) and packet[ARP].op == 2:
        ip = packet[ARP].psrc   # Paketin söylediği IP adresi
        mac = packet[ARP].hwsrc # Paketin söylediği MAC adresi

        # Daha önce bu IP için farklı bir MAC görmüş müydük?
        if ip in ip_mac_table and ip_mac_table[ip] != mac:
            print(f"[⚠️ ALERT] ARP Spoofing Detected! IP: {ip} was {ip_mac_table[ip]}, now {mac}")
        else:
            # İlk kez görüyorsak veya MAC eşleşiyorsa kayıt et
            ip_mac_table[ip] = mac

# Ana döngü - sürekli ARP paketlerini dinle
print("[*] Monitoring ARP packets for spoofing...")
sniff(filter="arp", prn=detect_arp_spoof, store=0)
