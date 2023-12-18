from jwcrypto import jwk
import json


def gen_key():
    key = jwk.JWK.generate(kty="RSA", alg="RS256", use="sig", size=2048)
    private_key = key.export_private()
    public_key = key.export_public()
    if isinstance(private_key, dict):
        private_key = json.dumps(private_key)
    if isinstance(public_key, dict):
        public_key = json.dumps(public_key)

    public_key = f"=== public key ===\n{json.dumps(json.loads(public_key), indent=2)}"
    private_key = (
        f"=== private key ===\n{json.dumps(json.loads(private_key), indent=2)}"
    )

    return public_key, private_key


if __name__ == "__main__":
    public_key, privateKey = gen_key()
    with open("./key.pub", "w") as f:
        f.write(public_key)
        print(f"public key save to {f.name}")
    with open("./key", "w") as f:
        f.write(privateKey)
        print(f"private key save to {f.name}")
