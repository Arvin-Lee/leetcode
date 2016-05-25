#!/usr/bin/env python
#encoding=utf-8

'''

Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

'''


from collections import  Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        # 使用排序  96 ms
        return sorted(s) == sorted(t)

        # 使用哈希表计数 Python Counter工具  112 ms
        # return Counter(s).items() == Counter(t).items()




def main():
    s = "hello world"
    t = " worldhello"

    solution = Solution()

    print solution.isAnagram(s, t)


if __name__ == "__main__":
    main()

