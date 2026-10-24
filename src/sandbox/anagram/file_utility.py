from pathlib import Path


def load_dictonary(file: str | Path) -> list[str]:
    content = Path(file).read_text(encoding="utf-8")
    output: list[str] = []
    for word in content.split("\n"):
        output.append(word.lower())

    return sorted(output)
