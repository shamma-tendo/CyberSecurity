import hashlib
from concurrent.futures import ThreadPoolExecutor

def try_password(args):
    password, target_hash, algo = args
    h = hashlib.new(algo, password.encode()).hexdigest()
    return password if h == target_hash else None

def crack_hash(target_hash, wordlist_file, algo="sha256", workers=8):
    with open(wordlist_file) as f:
        candidates = [line.strip() for line in f]

    tasks = [(pw, target_hash, algo) for pw in candidates]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for result in executor.map(try_password, tasks):
            if result:
                return result
    return None

# Example: create your own test hash & wordlist to audit password policies
# result = crack_hash(target_hash, "rockyou_sample.txt")