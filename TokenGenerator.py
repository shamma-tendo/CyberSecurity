import secrets
import hmac
import time

class CSRFProtection:
    def __init__(self, secret_key):
        self.secret_key = secret_key.encode()

    def generate_token(self, session_id):
        timestamp = str(int(time.time()))
        message = f"{session_id}:{timestamp}".encode()
        signature = hmac.new(self.secret_key, message, "sha256").hexdigest()
        return f"{timestamp}:{signature}"

    def validate_token(self, token, session_id, max_age=3600):
        try:
            timestamp, signature = token.split(":")
            if int(time.time()) - int(timestamp) > max_age:
                return False
            message = f"{session_id}:{timestamp}".encode()
            expected = hmac.new(self.secret_key, message, "sha256").hexdigest()
            return hmac.compare_digest(signature, expected)
        except (ValueError, IndexError):
            return False

csrf = CSRFProtection("my-secret-key")
token = csrf.generate_token("session123")
print("Token:", token)
print("Valid?", csrf.validate_token(token, "session123"))