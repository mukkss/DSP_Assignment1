from pathlib import Path
from typing import Tuple


def read_text_file(path: str) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return p.read_text(encoding="utf-8")


def write_text_file(path: str, content: str) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def default_output_paths(input_path: str, mode: str) -> Tuple[str, str]:
    """Return (output_path, suggested_filename) based on mode: 'encode' or 'decode'."""
    p = Path(input_path)
    if mode == "encode":
        out = p.with_name(p.stem + "_ascii.txt")
    else:
        out = p.with_name(p.stem + "_decoded.txt")
    return str(out), out.name