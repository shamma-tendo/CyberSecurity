import hashlib
def hash_password(password):
    salt = "some_random_salt"
    return haslib.sha256((password + salt) .encode()).hexdigest()

print(has_password("cyber-check"))
