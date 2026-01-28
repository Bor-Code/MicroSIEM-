import re
from datetime import datetime

class LogParser:
    def parse(self, ip, raw_log):
        print(f"DEBUG: Gelen Ham Veri -> '{raw_log.strip()}'")
        log_data = {
            "source_ip": ip,
            "raw": raw_log.strip(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "event_type": "INFO"
        }
        log_lower = raw_log.lower()
        if "failed password" in log_lower:
            log_data["event_type"] = "AUTH_FAILURE"
            match = re.search(r'from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', raw_log)
            if match:
                log_data["attacker_ip"] = match.group(1)    
        elif "accepted password" in log_lower:
            log_data["event_type"] = "AUTH_SUCCESS"

        return log_data