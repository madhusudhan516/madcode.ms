"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.

Link for the problem:
https://leetcode.com/problems/valid-anagram/
"""

from collections import Counter


class Solution:
    def valid_anagrams(self, s :str, t :str):
        """returns true both contain exact length and same frequency of characters else false."""
        return Counter(s) == Counter(t)     #counter is sub-class of dictionary.

obj = Solution()
s, t = map(str, input().split())
print(obj.valid_anagrams(s, t))
