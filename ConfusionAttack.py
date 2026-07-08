import jwt  # pip install pyjwt
import json
import base64

def demonstrate_alg_none_vuln():
    """Shows why servers must explicitly whitelist algorithms"""
    # A properly signed token
    secret = "server_secret_key"
    payload = {"user": "guest", "admin": False}
    token = jwt.encode(payload, secret, algorithm="HS256")
    print("Legit token:", token)

    # Attacker crafts a token with alg=none and no signature
    header = base64.urlsafe_b64encode(json.dumps({"alg": "none", "typ": "JWT"}).encode()).rstrip(b'=')
    forged_payload = base64.urlsafe_b64encode(json.dumps({"user": "admin", "admin": True}).encode()).rstrip(b'=')
    forged_token = header + b"." + forged_payload + b"."
    print("Forged token (alg=none):", forged_token.decode())

    # VULNERABLE verification (don't do this)
    try:
        decoded = jwt.decode(forged_token, options={"verify_signature": False})
        print("If server trusts this blindly:", decoded)
    except Exception as e:
        print("Properly configured library rejects it:", e)

    # SAFE verification - always specify allowed algorithms
    try:
        jwt.decode(forged_token, secret, algorithms=["HS256"])  # forces algorithm check
    except jwt.InvalidTokenError as e:
        print("✅ Correctly rejected:", e)

demonstrate_alg_none_vuln()