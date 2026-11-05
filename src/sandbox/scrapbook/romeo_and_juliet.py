from collections import Counter

from sandbox.scrapbook.shake_plays import PLAY


def main() -> None:
    """Print the 50 most frequent words in the play."""
    words = get_words(PLAY)
    ordered_words = words_frequency(words)
    top_n_words(ordered_words, 50)


def get_words(play: str) -> list[str]:
    """Split the text into a list of whitespace-separated words."""
    return play.split()


# First implamentation - works, but I found a better way
#
# def words_frequency(words: list[str]) -> Counter:
#     """Count how often each word appears and return a Counter."""
#     word_counter = {}
#     for word in words:
#         word_counter[word] = word_counter.get(word, 0) + 1
#     return Counter(word_counter)


def words_frequency(words: list[str]) -> Counter:
    """Count how often each word appears and return a Counter."""
    return Counter(words)


def top_n_words(word_and_frequency: Counter, n: int) -> None:
    """Print the n most common words with their counts."""
    for word, count in word_and_frequency.most_common(n):
        print(f"{word:<10} {count:>4}")


if __name__ == "__main__":
    main()
