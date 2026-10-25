import sys
from pathlib import Path

from sandbox.anagram.engine import find_anagram
from sandbox.anagram.file_utility import load_dictionary


def main() -> None:
    WORDS_FILE = Path(__file__).parent / "words.txt"
    WORDS = load_dictionary(WORDS_FILE)

    running = True

    ini_name = input("Please enter your full name: ")
    name = "".join(ini_name.lower().split())
    name = name.replace("-", "")
    limit = len(name)
    phrase: str = ""

    # Program loop
    while running:
        temp_prase = phrase.replace(" ", "")
        tp_len = len(temp_prase)

        if tp_len < limit:
            if tp_len > 0:
                print(f"Lenght of anagram phrase: {tp_len}")

            find_anagram(name, WORDS)

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


if __name__ == "__main__":
    main()
