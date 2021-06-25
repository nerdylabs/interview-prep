'''
Q5. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

LeetCode --> https://leetcode.com/problems/two-sum/

sample i/p --> nums = [2,7,11,15], target = 9
sample o/p --> [0, 1]

Difficulty --> Easy
'''


def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if seen.get(nums[i]) != None:
            return [seen[nums[i]], i]
        else:
            seen[diff] = i


print(two_sum([2, 7, 11, 15], 9))
