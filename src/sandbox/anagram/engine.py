from collections import Counter


def find_anagram(name: str, word_list: list[str]) -> list[str]:
    """Read name and world_list and dispaly all anagrams in name"""
    name_map = Counter(name)
    anagrams: list[str] = []

    for word in word_list:
        test: str = ""
        world_map = Counter(word.lower())
        for letter in word:
            if world_map[letter] <= name_map[letter]:
                test += letter
        if Counter(test) == world_map:
            anagrams.append(word)
    print(*anagrams, sep="\n")

    return anagrams


if __name__ == "__main__":
    pass
