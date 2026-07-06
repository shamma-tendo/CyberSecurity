import ssl
import socket
from datetime import datetime

def check_tls_certificate(hostname, port=443):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port), timeout=5) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()

            not_after = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            days_left = (not_after - datetime.now()).days

            issuer = dict(x[0] for x in cert['issuer'])
            subject = dict(x[0] for x in cert['subject'])

            print(f"Subject: {subject.get('commonName')}")
            print(f"Issuer: {issuer.get('commonName')}")
            print(f"Expires: {cert['notAfter']} ({days_left} days left)")
            print(f"TLS Version: {ssock.version()}")
            print(f"Cipher: {ssock.cipher()}")

            if days_left < 30:
                print("⚠️  Certificate expiring soon!")

            return cert

check_tls_certificate("example.com")