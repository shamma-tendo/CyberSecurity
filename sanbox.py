import os
import platform

def check_sandbox_indicators():
    indicators = []

    # Check for common VM artifacts
    vm_files = ["/usr/bin/VBoxControl", "/usr/bin/vmware-toolbox-cmd"]
    for f in vm_files:
        if os.path.exists(f):
            indicators.append(f"VM tool found: {f}")

    # Check CPU count (sandboxes often have minimal resources)
    cpu_count = os.cpu_count()
    if cpu_count and cpu_count <= 2:
        indicators.append(f"Low CPU count: {cpu_count} (possible sandbox)")

    # Check for common sandbox usernames/hostnames
    suspicious_names = ["sandbox", "malware", "virus", "test"]
    hostname = platform.node().lower()
    if any(name in hostname for name in suspicious_names):
        indicators.append(f"Suspicious hostname: {hostname}")

    return indicators

print(check_sandbox_indicators())