'''
Q15. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

sample i/p --> [2,2,1]
smaple o/p --> 1

Leetcode --> https://leetcode.com/problems/single-number/

Difficulty --> Easy
'''


def single_number(nums):
    '''
        Time --> O(n)
        space --> O(n)
    '''
    seen = {}
    for i in nums:
        if seen.get(i) != None:
            seen[i] += 1
        else:
            seen[i] = 1

    for i in seen.keys():
        if seen[i] == 1:
            return i


print(single_number([2, 2, 1]))

'''
Coming up with a solution that is linear in Time and constant in space is a bit difficult.
Refer the discussion tab for the question on the question page. A proper discussion for the same is done.
But I feel this solution is not that bad either.
'''
