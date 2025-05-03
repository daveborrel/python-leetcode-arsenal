import base64
import hmac
import hashlib
import time
import struct

def generate_totp(email: str) -> str:
    secret = (email + "SECRETKEY").encode('utf-8')
    timestep = int(time.time()) // 30
    msg = struct.pack(">Q", timestep)
    hmac_digest = hmac.new(secret, msg, hashlib.sha512).digest()
    offset = hmac_digest[-1] & 0x0F
    truncated_hash = hmac_digest[offset:offset + 4]
    code = struct.unpack(">I", truncated_hash)[0] & 0x7FFFFFFF
    return f"{code % 10**10:010d}"

def get_authorization_header(email: str) -> str:
    password = generate_totp(email)
    credentials = f"{email}:{password}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded}"

# Replace with your email
email = "example@gmail.com"
print(get_authorization_header(email))