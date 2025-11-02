from typing import List

def text_to_ascii(text: str) -> str:
    """Convert text to a space-separated ASCII numbers string.

    Raises ValueError if text contains non-ASCII characters (e.g., emojis) because
    the user opted out of emoji support.
    """
    if text is None:
        return ""

    # Ensure only ASCII characters
    try:
        text_bytes = text.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("Non-ASCII character detected. Emoji support is disabled.") from exc

    codes: List[str] = [str(b) for b in text_bytes]
    return " ".join(codes)