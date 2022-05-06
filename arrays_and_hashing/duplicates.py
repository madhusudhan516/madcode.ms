"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Link for the problem: https://leetcode.com/problems/contains-duplicate/
"""


class Solution:
    """This Solution class has containsDuplilcates method."""

    def __init__(self) -> None:
        pass

    def contains_duplicate(self, nums: tuple) -> bool:
        """
        containsDuplicate is a class method that returns true if list has duplicates else false.
        """
        _set = set()
        for i in nums:
            if i in _set:
                return True
            _set.add(i)
        return False


obj = Solution()
num_list: list = tuple(map(int, input().split()))
print(obj.contains_duplicate(num_list))
