'''
Q10. Maximum Subarray 

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

sample i/p --> [-2,1,-3,4,-1,2,1,-5,4]
sample o/p --> 6

leetcode --> https://leetcode.com/problems/maximum-subarray/

Difficulty --> Easy

Reference --> Kadane's Algorithm --> https://www.youtube.com/watch?v=86CQq3pKSUw
'''


def max_subarry(arr):
    curr_sum = max_ = arr[0]
    for i in range(1, len(arr)):
        curr_sum = max(arr[i], curr_sum + arr[i])
        if curr_sum > max_:
            max_ = curr_sum
    return max_


print(max_subarry([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
