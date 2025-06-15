import matplotlib.pyplot as plt
from collections import Counter
import re

# alerts.txt dosyasını oku
with open("alerts.txt", "r") as file:
    lines = file.readlines()

# IP adreslerini çek
ip_list = []
for line in lines:
    match = re.search(r"IP: ([\d.]+)", line)
    if match:
        ip_list.append(match.group(1))

# IP frekanslarını say
counter = Counter(ip_list)

# Görselleştir
plt.figure(figsize=(10, 5))
plt.bar(counter.keys(), counter.values())
plt.xlabel("Hedef IP Adresleri")
plt.ylabel("Saldırı Sayısı")
plt.title("ARP Spoofing Tespiti - IP Bazlı Saldırı Frekansı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("arp_alerts_chart.png")
plt.show()
