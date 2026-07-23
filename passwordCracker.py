from scapy.all import ARP, sniff

def process_packet(packet):
    if packet.haslayer(ARP) and packet[ARP].op == 2:  
        try:
            real_mac = packet[ARP].hwsrc
            response_mac = packet[ARP].hwsrc
            print(f"ARP reply: {packet[ARP].psrc} is-at {real_mac}")
        except IndexError:
            pass

