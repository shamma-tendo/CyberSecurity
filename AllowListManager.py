import ipaddress

class IPFilter:
    def __init__(self):
        self.blocklist = set()
        self.allowlist = set()

    def block(self, ip_or_range):
        self.blocklist.add(ipaddress.ip_network(ip_or_range, strict=False))

    def allow(self, ip_or_range):
        self.allowlist.add(ipaddress.ip_network(ip_or_range, strict=False))

    def is_allowed(self, ip):
        addr = ipaddress.ip_address(ip)
        if any(addr in net for net in self.blocklist):
            return False
        if self.allowlist and not any(addr in net for net in self.allowlist):
            return False
        return True

filt = IPFilter()
filt.block("192.168.1.0/24")
print(filt.is_allowed("192.168.1.5"))   # False
print(filt.is_allowed("10.0.0.1"))      # True