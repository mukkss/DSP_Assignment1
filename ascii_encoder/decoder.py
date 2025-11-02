from typing import List

def ascii_to_text(ascii_input: str) -> str:
    """Convert a space-separated string of ASCII numbers into text.

    Raises ValueError for invalid integers or out-of-range byte values.
    """
    if ascii_input is None:
        return ""

    ascii_input = ascii_input.strip()
    if ascii_input == "":
        return ""

    parts = ascii_input.split()
    bytes_list: List[int] = []
    for p in parts:
        try:
            n = int(p)
        except ValueError as exc:
            raise ValueError(f"Invalid ASCII code: '{p}'. Must be integer.") from exc
        if not 0 <= n <= 127:
            raise ValueError(f"ASCII code out of range (0-127): {n}")
        bytes_list.append(n)

    return bytes(bytes_list).decode("ascii")