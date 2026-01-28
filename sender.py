import socket
import time
import random

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5140

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[*] Saldırı Simülatörü Başlatıldı -> Hedef: {TARGET_IP}:{TARGET_PORT}")
print("[*] Loglar gönderiliyor... (Durdurmak için CTRL+C)")

ips = ["192.168.1.50", "10.0.0.5", "172.16.0.23", "45.33.22.11", "185.22.11.33"]

try:
    count = 1
    while True:
        fake_ip = random.choice(ips)
        
        log_message = f"Oct 28 22:14:15 server sshd[123]: Failed password for root from {fake_ip}"
        
        sock.sendto(log_message.encode(), (TARGET_IP, TARGET_PORT))
        print(f"[{count}] Saldırı Logu Gönderildi: {fake_ip}")
        
        count += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[!] Simülasyon durduruldu.")