class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

    def containsDuplicateBetter(self, nums: list[int]) -> bool:
        for n in range(len(nums)):
            for c in nums[n + 1 :]:
                if c == nums[n]:
                    return True
        return False

    def containsDuplicateBackup(self, nums: list[int]) -> bool:
        for i, n in enumerate(nums):
            check = nums[:]
            del check[i]
            for c in check:
                if c == n:
                    return True
        return False


# 1️⃣
# Greatest Common Divisor
# Create an algorithm that finds the GCD (Greatest Common Divisor) of two integers.


# 2️⃣
# Palindrome
# Create an algorithm that checks if an integer is a palindrome.


# 3️⃣
# String Permutations
# Create an algorithm that checks whether or not a given string is a permutation of another string.
