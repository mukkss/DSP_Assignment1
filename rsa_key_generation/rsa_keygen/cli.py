import argparse
from colorama import Fore, Style
from rsa_keygen.generator import (
    generate_rsa_keypair,
    serialize_private_key,
    serialize_public_key,
)
from rsa_keygen.file_handler import save_key_to_file
from pathlib import Path


def run_cli():
    parser = argparse.ArgumentParser(
        description="RSA Key Pair Generator (CLI Tool)"
    )

    parser.add_argument(
        "-s", "--size", type=int, default=2048,
        help="Key size in bits (1024, 2048, 4096)"
    )
    parser.add_argument(
        "-o", "--out", type=str, default=".",
        help="Output directory for keys"
    )
    parser.add_argument(
        "-p", "--password", type=str,
        help="Password to encrypt private key (optional)"
    )
    parser.add_argument(
        "--show", choices=["public", "private"],
        help="Show generated key in terminal"
    )

    args = parser.parse_args()

    print(Fore.CYAN + f"🔐 Generating RSA key pair ({args.size}-bit)...")
    private_key, public_key = generate_rsa_keypair(args.size)

    priv_bytes = serialize_private_key(private_key, args.password)
    pub_bytes = serialize_public_key(public_key)

    output_dir = Path(args.out) / "keys"
    output_dir.mkdir(parents=True, exist_ok=True)

    priv_path = output_dir / "private_key.pem"
    pub_path = output_dir / "public_key.pem"

    save_key_to_file(priv_bytes, priv_path)
    save_key_to_file(pub_bytes, pub_path)

    print(Fore.GREEN + f"\n✅ RSA Keys generated successfully!")
    print(Fore.YELLOW + f"Private Key → {priv_path}")
    print(Fore.YELLOW + f"Public Key  → {pub_path}" + Style.RESET_ALL)

    # Optional: show key in terminal
    if args.show:
        print(Fore.CYAN + "\n📜 Key Content:\n" + Style.RESET_ALL)
        if args.show == "public":
            print(pub_bytes.decode())
        elif args.show == "private":
            print(priv_bytes.decode())
