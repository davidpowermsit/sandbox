import sys
from pathlib import Path

from sandbox.anagram.engine import find_anagram
from sandbox.anagram.file_utility import load_dictonary


def main() -> None:
    WORDS_FILE = Path(__file__).parent / "words.txt"
    WORDS = load_dictonary(WORDS_FILE)

    running = True

    ini_name = input("Please enter your full name: ")
    name = "".join(ini_name.lower().split())
    name = name.replace("-", "")
    limit = len(name)
    phrase: str = ""

    # Program loop
    while running:
        temp_prase = phrase.replace(" ", "")
        if len(temp_prase) < limit:
            if len(temp_prase) > 0:
                print(f"Lenght of anagram phrase: {len(temp_prase)}")

            anagrams = find_anagram(name, WORDS)
            display_anagram_information(name, anagrams)

            if len(temp_prase) > 0:
                print(f"Current anagram phrase is: {phrase}")

            choice, name = process_choice(name)
            phrase += choice + " "

        elif len(temp_prase) == limit:
            print("Final Anagram Phrase: ")
            print(phrase, file=sys.stderr)
            print()
            try_again = input("Try again? (Press Enter else 'n' to quit.): ")
            if try_again.lower() == "n":
                running = False
                sys.exit()
            else:
                main()


def process_choice(name: str) -> tuple[str, str]:
    while True:
        choice = input("Make a choice else Enter to start over or # to end: ")
        if choice == "":
            main()
        elif choice == "#":
            sys.exit()
        else:
            candidate = "".join(choice.lower().split())
            left_over_list = list(name)
            for letter in candidate:
                if letter in left_over_list:
                    left_over_list.remove(letter)
            if len(name) - len(left_over_list) == len(candidate):
                break
            else:
                print("That choice will not work. Choose valid word from list.")

    name = "".join(left_over_list)
    return choice, name


def display_anagram_information(name: str, anagrams: list[str]) -> None:
    print(*anagrams, sep="\n")
    print()
    print(f"Remaining letters: {name}")
    print(f"No of remaining letters: {len(name)}")
    print(f"No of remaining letters (real world) anagrams: {len(anagrams)}")


if __name__ == "__main__":
    main()
