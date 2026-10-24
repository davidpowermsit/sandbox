from pathlib import Path


def load_dictonary(file: str | Path) -> set[str]:
    content = Path(file).read_text(encoding="utf-8")
    output: set[str] = set()
    for word in content.split("\n"):
        output.add(word)

    output.update({"a", "i"})
    return output
