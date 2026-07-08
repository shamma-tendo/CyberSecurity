from scapy.all import IP, TCP, Raw, send
import random

def fuzz_tcp_payload(target_ip, target_port, iterations=100):
    """Send malformed payloads to test a service's robustness — YOUR OWN test server only"""
    for i in range(iterations):
        payload_size = random.randint(1, 2000)
        payload = bytes(random.getrandbits(8) for _ in range(payload_size))
        
        pkt = IP(dst=target_ip) / TCP(dport=target_port, flags="PA") / Raw(load=payload)
        send(pkt, verbose=0)

# fuzz_tcp_payload("127.0.0.1", 8080, iterations=50)  # against your own local service