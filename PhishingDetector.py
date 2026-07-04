import re
from urllib.parse import urlparse

def check_suspicious_url(url):
    flags = []
    parsed = urlparse(url)

    if re.match(r"^\d+\.\d+\.\d+\.\d+$", parsed.netloc):
        flags.append("Uses raw IP address instead of domain")

    if len(url) > 75:
        flags.append("Unusually long URL")

    if parsed.netloc.count('-') > 2:
        flags.append("Multiple hyphens in domain (common in fake domains)")

    suspicious_keywords = ["login", "verify", "account", "secure", "update"]
    if any(word in url.lower() for word in suspicious_keywords) and "https" not in url:
        flags.append("Sensitive keywords without HTTPS")

    return flags

test_url = "http://192.168.1.1/verify-account-update-secure"
print(check_suspicious_url(test_url))