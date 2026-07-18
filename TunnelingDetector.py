from collections import defaultdict
import re

class DNSTunnelDetector:
    def __init__(self):
        self.queries = defaultdict(list)

    def analyze_query(self, domain, query_type="A"):
        flags = []
        
      
        subdomain = domain.split('.')[0]
        if len(subdomain) > 50:
            flags.append("Abnormally long subdomain (possible encoded payload)")
        
     
        if re.match(r'^[a-f0-9]{32,}$', subdomain):
            flags.append("Hex-like high-entropy subdomain")
        
       
        if query_type == "TXT":
            flags.append("TXT query (commonly abused for tunneling)")
        
        base_domain = '.'.join(domain.split('.')[-2:])
        self.queries[base_domain].append(domain)
      
        if len(self.queries[base_domain]) > 100:
            flags.append(f"High query volume to {base_domain} ({len(self.queries[base_domain])} queries)")
        
        return flags

detector = DNSTunnelDetector()
test_queries = [
    ("4d616c77617265446174614865726531323334.evil-domain.com", "TXT"),
    ("www.google.com", "A"),
]
for domain, qtype in test_queries:
    result = detector.analyze_query(domain, qtype)
    if result:
        print(f"{domain}: {result}")
