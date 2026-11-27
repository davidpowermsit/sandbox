from collections import Counter


class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

    def contains_duplicate_better(self, nums: list[int]) -> bool:
        for n in range(len(nums)):
            for c in nums[n + 1 :]:
                if c == nums[n]:
                    return True
        return False

    def contains_duplicate_backup(self, nums: list[int]) -> bool:
        for i, n in enumerate(nums):
            check = nums[:]
            del check[i]
            for c in check:
                if c == n:
                    return True
        return False


# 1 - Understand the problem
# 2 - Plan a step-by-step algorithm
# 3 - Implement the algorithm
# 4 - Review and optimize


# 1️⃣
# Greatest Common Divisor
# Create an algorithm that finds the GCD (Greatest Common Divisor) of two integers.


class GreatestCommonDivisor:
    def solution(self, a: int, b: int) -> int:
        if a <= 0 or b <= 0:
            raise ValueError("a and b must be positive")

        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                return i
        # Exception to satisfy mypy
        raise AssertionError("unreachable: 1 divides everything")

    def solution_first(self, a: int, b: int) -> int:
        # Get all divisors for a and b
        candidates = [a, b]
        divisors: dict[int, set[int]] = {}
        for candidate in candidates:
            divisors[candidate] = set()
            for value in range(1, candidate + 1):
                if candidate % value == 0:
                    divisors[candidate].add(value)
        # Find the greatest common divisor
        common = divisors[a] & divisors[b]
        lcd = max(common)
        return lcd


# 2️⃣
# Palindrome
# Create an algorithm that checks if an integer is a palindrome.


class Palindrome:
    def solution(self, candidate: int) -> bool:
        return str(candidate) == str(candidate)[::-1]


# 3️⃣
# String Permutations
# Create an algorithm that checks whether or not a given string is a permutation of another string.


class StringPermutations:
    def solution(self, a: str, b: str) -> bool:
        a_dict = Counter(a)
        b_dict = Counter(b)
        return a_dict == b_dict
