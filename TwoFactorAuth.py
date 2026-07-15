import pyotp

def setup_2fa():
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret)
    print(f"Secret (save this): {secret}")
    print(f"Current code: {totp.now()}")
    return secret

def verify_2fa(secret, code):
    totp = pyotp.TOTP(secret)
    return totp.verify(code)

secret = setup_2fa()
