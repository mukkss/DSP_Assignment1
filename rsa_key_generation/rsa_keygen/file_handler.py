from pathlib import Path

def save_key_to_file(key_bytes, filename):
    path = Path(filename)
    with open(path, "wb") as f:
        f.write(key_bytes)
    return str(path)
