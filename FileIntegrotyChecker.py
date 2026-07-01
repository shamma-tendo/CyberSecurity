import hashlib

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

# Save this hash somewhere safe, compare later to detect changes
print(get_file_hash("example.txt"))