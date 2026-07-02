import socket
from datetime import datetime

def honeypot(port=2222):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("0.0.0.0", port))
    s.listen(5)
    print(f"Honeypot listening on port {port}...")

    while True:
        conn, addr = s.accept()
        print(f"[{datetime.now()}] Connection attempt from {addr}")
        conn.send(b"SSH-2.0-OpenSSH_7.4\r\n")  # fake banner
        conn.close()

# honeypot()  # run this only on your own machine/network