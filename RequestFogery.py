import ipaddress
from urllib.parse import urlparse
import socket

def is_safe_url(url, blocked_ranges=None):
    """A more robust SSRF check than simple string matching"""
    blocked_ranges = blocked_ranges or [
        "127.0.0.0/8", "10.0.0.0/8", "172.16.0.0/12",
        "192.168.0.0/16", "169.254.0.0/16", "::1/128"
    ]
    
    parsed = urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return False, "No hostname"

    try:
        # Resolve DNS to catch DNS-rebinding attempts
        resolved_ip = socket.gethostbyname(hostname)
        ip_obj = ipaddress.ip_address(resolved_ip)
        
        for blocked_range in blocked_ranges:
            if ip_obj in ipaddress.ip_network(blocked_range):
                return False, f"Resolves to blocked range: {blocked_range}"
        
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_link_local:
            return False, "Private/loopback/link-local address"
            
    except (socket.gaierror, ValueError) as e:
        return False, f"Resolution error: {e}"

    return True, "OK"

test_urls = [
    "http://169.254.169.254/latest/meta-data/",  # cloud metadata endpoint
    "http://localhost:8080/admin",
    "https://example.com",
]
for url in test_urls:
    safe, reason = is_safe_url(url)
    print(f"{url}: {'✅ safe' if safe else '❌ blocked'} ({reason})")