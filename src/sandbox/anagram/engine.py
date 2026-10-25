from collections import Counter


def find_anagram(name: str, word_list: list[str]) -> list[str]:
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

    return anagrams


if __name__ == "__main__":
    pass
