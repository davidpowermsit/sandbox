from collections import Counter


def find_anagram(name: str, word_list: list[str]) -> None:
    """Read name and word_list and dispaly all anagrams in name"""
    name_map = Counter(name)
    anagrams: list[str] = []

    for word in word_list:
        test: str = ""
        word_map = Counter(word.lower())
        for letter in word:
            if word_map[letter] <= name_map[letter]:
                test += letter
        if Counter(test) == word_map:
            anagrams.append(word)

    for anagram in anagrams:
        print(f"- {anagram}")
    print()
    print(f"Remaining letters: {name}")
    print(f"No of remaining letters: {len(name)}")
    print(f"No of remaining letters (real world) anagrams: {len(anagrams)}")


if __name__ == "__main__":
    pass
