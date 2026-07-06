import os
import stat
import subprocess

def check_suid_binaries():
    """Find SUID binaries — a classic privesc vector if misconfigured"""
    suspicious = []
    common_dirs = ["/usr/bin", "/usr/sbin", "/bin", "/sbin"]
    for directory in common_dirs:
        if not os.path.exists(directory):
            continue
        for f in os.listdir(directory):
            path = os.path.join(directory, f)
            try:
                if os.path.isfile(path) and os.stat(path).st_mode & stat.S_ISUID:
                    suspicious.append(path)
            except (PermissionError, FileNotFoundError):
                continue
    return suspicious

def check_world_writable_files(directory="/etc"):
    """World-writable config files are a red flag"""
    findings = []
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            try:
                mode = os.stat(path).st_mode
                if mode & stat.S_IWOTH:
                    findings.append(path)
            except (PermissionError, FileNotFoundError):
                continue
    return findings

print("SUID binaries found:", check_suid_binaries()[:10])
print("World-writable files in /etc:", check_world_writable_files()[:10])