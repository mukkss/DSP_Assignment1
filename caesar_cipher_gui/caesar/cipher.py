from typing import Tuple


def validate_ascii_text(text: str) -> None:
    """Raise ValueError if text contains non-ascii characters."""
    try:
        text.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("Non-ASCII character detected. This tool supports ASCII text only.") from exc


def _normalize_shift(shift: int) -> int:
    # Keep shift within 0-25
    return shift % 26


def encrypt(plaintext: str, shift: int) -> str:
    """Encrypt plaintext using Caesar cipher with given shift. Only letters A-Z / a-z change.

    Non-letter ASCII characters (spaces, punctuation, digits) are left unchanged.
    """
    if plaintext is None:
        return ""
    validate_ascii_text(plaintext)
    s = _normalize_shift(shift)
    result_chars = []
    for ch in plaintext:
        code = ord(ch)
        # uppercase
        if 65 <= code <= 90:
            base = 65
            result_chars.append(chr((code - base + s) % 26 + base))
        # lowercase
        elif 97 <= code <= 122:
            base = 97
            result_chars.append(chr((code - base + s) % 26 + base))
        else:
            result_chars.append(ch)
    return "".join(result_chars)


def decrypt(ciphertext: str, shift: int) -> str:
    """Decrypt ciphertext using Caesar cipher with given shift."""
    return encrypt(ciphertext, -shift)


# Optional helper returning both
def transform(text: str, shift: int, mode: str) -> str:
    if mode == "encrypt":
        return encrypt(text, shift)
    elif mode == "decrypt":
        return decrypt(text, shift)
    else:
        raise ValueError("mode must be 'encrypt' or 'decrypt'")