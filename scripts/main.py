from os import error
import sys

from scripts import generate_key
from scripts import generate_token


def run():
    arg = sys.argv[1]
    if arg == "key":
        public_key, privateKey = generate_key.gen_key()
        with open("./key.pub", "w") as f:
            f.write(public_key)
            print(f"public key save to {f.name}")
        with open("./key", "w") as f:
            f.write(privateKey)
            print(f"private key save to {f.name}")
    elif arg == "token":
        JWT = generate_token.gen_token()
        with open("./token", "w") as f:
            f.write(JWT)
            print(f"token save to {f.name}")
    elif arg == "send":
        error("not implemented")
    else:
        print("invalid command")


if __name__ == "__main__":
    run()
