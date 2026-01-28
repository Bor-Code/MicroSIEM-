class ThreatDetector:
    def __init__(self):
        self.failed_login_attempts = {}

    def analyze(self, parsed_log):
        if parsed_log["event_type"] == "AUTH_FAILURE":
            attacker = parsed_log.get("attacker_ip", "Unknown")
            
            if attacker in self.failed_login_attempts:
                self.failed_login_attempts[attacker] += 1
            else:
                self.failed_login_attempts[attacker] = 1

            count = self.failed_login_attempts[attacker]
            if count >= 5:
                return self.alert(attacker, count)      
        return None

    def alert(self, ip, count):
        alert_msg = f"[KRİTİK ALARM] Brute Force Tespiti! IP: {ip} - Deneme: {count}"
        print("\033[91m" + alert_msg + "\033[0m") # Kırmızı renkli çıktı
        return alert_msg