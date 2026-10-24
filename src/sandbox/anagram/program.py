from pathlib import Path

from sandbox.anagram.engine import is_anagram
from sandbox.anagram.file_utility import load_dictonary

WORDS_FILE = Path(__file__).parent / "words.txt"

# Load a dictionary file
# Accept a name from user
# Set limit = length of name
# Start empty list to hold anagram phrase
# While length of phrase < limit:
#     Generate list of dictionary words that fit in name
#     Present words to user
#     Present remaining letters to user
#     Present current phrase to user
#     Ask user to input word or start over
#     If user input can be made from remaining letters:
#         Accept choice of new word or words from user
#         Remove letters in choice from letters in name
#         Return choice and remaining letters in name
#     If choice is not a valid selection:
#         Ask user for new choice or let user start over
#     Add choice to phrase and show to user
#     Generate new list of words and repeat process
# When phrase length equals limit value:
#     Display final phrase
#     Ask user to start over or to exit


def main() -> None:
    target = input("Please enter a word: ").strip()
    words = load_dictonary(WORDS_FILE)
    collection: list[str] = []
    for word in words:
        if is_anagram(target, word):
            collection.append(word)
    if collection:
        print(f"These are the anagrams found for the word '{target}'")
        for item in sorted(collection):
            print(f"- {item}")
    else:
        print(f"These are no anagrams found for the word '{target}'")


if __name__ == "__main__":
    main()
