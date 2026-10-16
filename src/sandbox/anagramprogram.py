from pathlib import Path

from sandbox.anagramfinder import is_anagram


def load_dictonary() -> list[str]:
    content = Path("words.txt").read_text(encoding="utf-8")
    output: list[str] = []
    for word in content.split("\n"):
        output.append(word)
    return output


def main() -> None:
    target = input("Please enter a word: ").strip()
    words = load_dictonary()
    collection: list[str] = []
    for word in words:
        if is_anagram(target, word):
            collection.append(word)
    if collection:
        print(f"These are the anagrams found for the word {target}")
        for item in collection:
            print(f"- {item}")
    else:
        print(f"These are no anagrams found for the word {target}")


if __name__ == "__main__":
    main()
