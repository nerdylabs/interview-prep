'''
Q18. Almost a Palindrome

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

sample i/p --> 'aba'
sample o/p --> true

sample i/p --> "abca"
sample o/[ --> true
Explanation --> You could delete the character 'c'.

Leetcode --> https://leetcode.com/problems/valid-palindrome-ii/
Difficulty --> Easy
'''


def check_palindrome(x, left, right):
    while left <= right:
        if x[left] != x[right]:
            return False

        left += 1
        right -= 1
    return True


def validPalindrome(s):
    x = ""
    li = [".", ",", "?", "/", "\\", "!", "@", "#", "$", "%", "^", "&", "*",
          "(", ")", "_", "-", "{", "}", "[", "]", "\'", "\"", ":", " ", ";", "`"]
    for i in s:
        if i in li:
            continue
        else:
            x += i.lower()

    left = 0
    right = len(x) - 1
    while left <= right:
        if x[left] != x[right]:
            return check_palindrome(x, left+1, right) or check_palindrome(x, left, right-1)
        left += 1
        right -= 1

    return True
