'''
Q17. 
Given a string s, return the longest palindromic substring in s.

sample i/p --> "babad"
sample o/p --> Output: "bab"
Note: "aba" is also a valid answer.

Leetcode --> https://leetcode.com/problems/longest-palindromic-substring/

Difficulty --> Medium
Explication of this solution --> https://leetcode.com/problems/longest-palindromic-substring/solution/
                             --> https://www.youtube.com/watch?v=y2BD4MJqV20
'''


def isPalindrome(s, left, right):
    if s == None or left > right:
        return 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1


def get_longest_palindrome(s):
    if s == None or len(s) < 1:
        return ""
    start = 0
    end = 0
    for i in range(len(s)):
        len1 = isPalindrome(s, i, i)
        len2 = isPalindrome(s, i, i+1)
        len_ = max(len1, len2)
        if len_ > end-start:
            start = i - ((len_ - 1)//2)
            end = i + (len_//2)
    return s[start:end+1]
