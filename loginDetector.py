from collections import defaultdict
from datetime import datetime

def detect_brute_force(logfile, threshold=5):
    attempts = defaultdict(list)
    with open(logfile) as f:
        for line in f:
            if "FAILED_LOGIN" in line:
                parts = line.split()
                ip = parts[0]
                timestamp = parts[1]
                attempts[ip].append(timestamp)

    for ip, times in attempts.items():
        if len(times) >= threshold:
            print(f"⚠️  Possible brute force from {ip}: {len(times)} failed attempts")

# Example log line format: "192.168.1.5 2026-07-02T10:15:00 FAILED_LOGIN user=admin"
detect_brute_force("auth.log")