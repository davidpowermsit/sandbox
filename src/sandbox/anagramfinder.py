def is_anagram(target: str, candidate: str) -> bool:

    # Ensure words are both lowercase
    target = target.lower()
    candidate = candidate.lower()

    # find lenght of both strings
    # if lenghts are not equil return false
    # if lenghts are equil proceed
    if len(target) != len(candidate):
        return False

    # for each letter in the target word count its occurances and store in dict
    # do this again for the candidate word
    target_analysis: dict[str, int] = {}
    for letter in target:
        target_analysis[letter] = target.count(letter)

    candidate_analysis: dict[str, int] = {}
    for letter in candidate:
        candidate_analysis[letter] = candidate.count(letter)

    # compare the two dicts
    # if they are equal then we found an anagram and we return True
    # else we return False
    return target_analysis == candidate_analysis


if __name__ == "__main__":
    pass
