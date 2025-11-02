import sys
from colorama import init as colorama_init, Fore, Style
from ascii_encoder.encoder import text_to_ascii
from ascii_encoder.decoder import ascii_to_text
from ascii_encoder.file_handler import read_text_file, write_text_file, default_output_paths
from ascii_encoder.logger_config import get_logger

colorama_init(autoreset=True)
logger = get_logger("ascii-cli")

BANNER = f"{Fore.CYAN}{Style.BRIGHT}==== ASCII TOOL ===={Style.RESET_ALL}"
MENU = f"""
{Fore.YELLOW}[1]{Style.RESET_ALL} 🔐 Encode Text
{Fore.YELLOW}[2]{Style.RESET_ALL} 🔓 Decode Text
{Fore.YELLOW}[3]{Style.RESET_ALL} 📄 Encode File
{Fore.YELLOW}[4]{Style.RESET_ALL} 📁 Decode File
{Fore.YELLOW}[0]{Style.RESET_ALL} ❌ Exit
"""


def prompt(msg: str) -> str:
    try:
        return input(msg)
    except EOFError:
        return ""


def encode_text_flow():
    text = prompt(f"{Fore.GREEN}Enter text to encode:{Style.RESET_ALL} ")
    try:
        out = text_to_ascii(text)
        print(f"\n{Fore.MAGENTA}Encoded ASCII:{Style.RESET_ALL} {out}\n")
        logger.info("Encoded text input")
    except ValueError as exc:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} {exc}")
        logger.error("Encoding error: %s", exc)


def decode_text_flow():
    ascii_in = prompt(f"{Fore.GREEN}Enter space-separated ASCII numbers:{Style.RESET_ALL} ")
    try:
        out = ascii_to_text(ascii_in)
        print(f"\n{Fore.MAGENTA}Decoded Text:{Style.RESET_ALL} {out}\n")
        logger.info("Decoded ASCII input")
    except ValueError as exc:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} {exc}")
        logger.error("Decoding error: %s", exc)


def encode_file_flow():
    path = prompt(f"{Fore.GREEN}Enter path to text file to encode:{Style.RESET_ALL} ")
    try:
        text = read_text_file(path)
        out = text_to_ascii(text)
        out_path, suggested = default_output_paths(path, "encode")
        write_text_file(out_path, out)
        print(f"{Fore.MAGENTA}Written encoded ASCII to:{Style.RESET_ALL} {out_path}")
        logger.info("Encoded file %s -> %s", path, out_path)
    except Exception as exc:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} {exc}")
        logger.error("File encode error: %s", exc)


def decode_file_flow():
    path = prompt(f"{Fore.GREEN}Enter path to ASCII file to decode:{Style.RESET_ALL} ")
    try:
        ascii_in = read_text_file(path)
        out = ascii_to_text(ascii_in)
        out_path, suggested = default_output_paths(path, "decode")
        write_text_file(out_path, out)
        print(f"{Fore.MAGENTA}Written decoded text to:{Style.RESET_ALL} {out_path}")
        logger.info("Decoded file %s -> %s", path, out_path)
    except Exception as exc:
        print(f"{Fore.RED}Error:{Style.RESET_ALL} {exc}")
        logger.error("File decode error: %s", exc)


def main():
    print(BANNER)
    while True:
        print(MENU)
        choice = prompt(f"{Fore.CYAN}Select an option:{Style.RESET_ALL} ")
        if choice == "1":
            encode_text_flow()
        elif choice == "2":
            decode_text_flow()
        elif choice == "3":
            encode_file_flow()
        elif choice == "4":
            decode_file_flow()
        elif choice == "0":
            print(f"{Fore.GREEN}Goodbye!{Style.RESET_ALL}")
            sys.exit(0)
        else:
            print(f"{Fore.RED}Invalid option. Try again.{Style.RESET_ALL}")


if __name__ == "__main__":
    main()