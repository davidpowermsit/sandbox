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


def is_anagram(target: str, candidate: str) -> bool:

    # Ensure words are both lowercase
    target = target.lower()
    candidate = candidate.lower()

    # find lenght of both strings
    # if lenghts are not equil return false
    # if lenghts are equil proceed
    # check if words are identical
    if len(target) != len(candidate) or target == candidate:
        return False

    # for each letter in the target word count its occurances and store in dict
    # do this again for the candidate word
    target_analysis = Counter(target)
    candidate_analysis = Counter(candidate)

    # compare the two dicts
    # if they are equal then we found an anagram and we return True
    # else we return False
    return target_analysis == candidate_analysis


if __name__ == "__main__":
    pass
