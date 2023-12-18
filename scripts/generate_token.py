import jwt
from jwt.algorithms import RSAAlgorithm
import time
import os

with open("./key", "r") as f:
    privateKey = f.read()

headers = {"alg": "RS256", "typ": "JWT", "kid": os.environ.get("LINE_KID")}
payload = {
    "iss": os.environ.get("LINE_CHANNEL_ID"),
    "sub": os.environ.get("LINE_CHANNEL_ID"),
    "aud": "https://api.line.me/",
    "exp": int(time.time()) + (60 * 30),
    "token_exp": 60 * 60 * 24 * 30,
}

key = RSAAlgorithm.from_jwk(privateKey)
JWT = jwt.encode(payload, key, algorithm="RS256", headers=headers, json_encoder=None)  # type: ignore
with open("./token", "w") as f:
    f.write(JWT)
    print(f"token save to {f.name}")
