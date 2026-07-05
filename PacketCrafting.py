from scapy.all import IP, TCP, send, sr1

def send_syn_probe(target_ip, target_port):
    packet = IP(dst=target_ip) / TCP(dport=target_port, flags="S")
    response = sr1(packet, timeout=2, verbose=0)
    if response is None:
        return "No response (filtered)"
    elif response.haslayer(TCP):
        if response[TCP].flags == "SA":
            return "Open"
        elif response[TCP].flags == "RA":
            return "Closed"
    return "Unknown"

# Only run against systems you own or have written permission to test
# print(send_syn_probe("127.0.0.1", 80))