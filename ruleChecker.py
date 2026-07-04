import re

waf_rules = {
    "SQL Injection": r"(\bunion\b.*\bselect\b|\bor\b\s+1=1|--|\bdrop\b\s+\btable\b)",
    "XSS": r"(<script.*?>|javascript:|onerror\s*=)",
    "Path Traversal": r"(\.\./|\.\.\\)",
    "Command Injection": r"(;|\||&&|\$\()",
}

def check_request(payload):
    triggered = []
    for rule_name, pattern in waf_rules.items():
        if re.search(pattern, payload, re.IGNORECASE):
            triggered.append(rule_name)
    return triggered

test_inputs = [
    "search?q=hello",
    "search?q=<script>alert(1)</script>",
    "id=1 OR 1=1--",
    "file=../../etc/passwd",
]

for test in test_inputs:
    result = check_request(test)
    print(f"{test!r} -> {result if result else 'clean'}")