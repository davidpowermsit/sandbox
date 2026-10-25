from pathlib import Path


def load_dictionary(file: str | Path) -> list[str]:
    content = Path(file).read_text(encoding="utf-8")
    return sorted(word.lower() for word in content.splitlines() if word.strip())
