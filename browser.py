import base64
import hashlib
import json
import random
import string

from Crypto.Cipher import AES


def encrypt(data, key):
    data = data + chr(16 - len(data) % 16) * (16 - len(data) % 16)

    salt = b"".join(random.choice(string.ascii_lowercase).encode() for _ in range(8))
    salted, dx = b"", b""
    while len(salted) < 48:
        dx = hashlib.md5(dx + key.encode() + salt).digest()
        salted += dx

    key = salted[:32]
    iv = salted[32 : 32 + 16]
    aes = AES.new(key, AES.MODE_CBC, iv)

    encrypted_data = {
        "ct": base64.b64encode(aes.encrypt(data.encode())).decode("utf-8"),
        "iv": iv.hex(),
        "s": salt.hex(),
    }
    return json.dumps(encrypted_data, separators=(",", ":"))


def decrypt(data, key):
    data = json.loads(data)
    dk = key.encode() + bytes.fromhex(data["s"])
    md5 = [hashlib.md5(dk).digest()]
    result = md5[0]
    for i in range(1, 3 + 1):
        md5.insert(i, hashlib.md5((md5[i - 1] + dk)).digest())
        result += md5[i]

    aes = AES.new(result[:32], AES.MODE_CBC, bytes.fromhex(data["iv"]))
    data = aes.decrypt(base64.b64decode(data["ct"]))
    return data
