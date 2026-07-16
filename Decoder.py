import base64
import json

def decode_jwt(token):
    header, payload, signature = token.split(".")
    def pad_decode(segment):
        segment += "=" * (-len(segment) % 4)
        return json.loads(base64.urlsafe_b64decode(segment))

    print("Header:", pad_decode(header))
    print("Payload:", pad_decode(payload))
    print("Signature (still encoded):", signature)


decode_jwt("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4ifQ.abc123")
