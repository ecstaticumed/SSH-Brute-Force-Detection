import subprocess
import re
from collections import defaultdict
import time

THRESHOLD = 5
CHECK_INTERVAL = 10  # seconds
blocked_ips = set()
failed_attempts = defaultdict(int)

def block_ip(ip):
    if ip not in blocked_ips:
        print(f"[ALERT] Blocking SSH brute-force IP: {ip}")
        subprocess.run(["ufw", "deny", "from", ip],
                       stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        blocked_ips.add(ip)

print("[*] Real-time SSH Brute Force Detection Started...")
print("[*] Monitoring SSH authentication logs...\n")

while True:
    try:
        # Kali Linux (systemd journal)
        cmd = ["journalctl", "-u", "ssh", "--since", "1 min ago", "--no-pager"]
        logs = subprocess.check_output(cmd, text=True)

        for line in logs.splitlines():
            if "Failed password" in line:
                ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    ip = ip_match.group(1)
                    failed_attempts[ip] += 1

                    if failed_attempts[ip] >= THRESHOLD:
                        block_ip(ip)

        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("\n[!] Detection stopped by user")
        break
