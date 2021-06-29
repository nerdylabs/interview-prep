'''
Q14.Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

sample i/p --> nums = [1,3,5,6], target = 5
sample o/p --> 2

sample i/p --> nums = [1,3,5,6], target = 2
sample o/p --> 1

Leetcode --> https://leetcode.com/problems/search-insert-position/

Difficulty --> Easy
'''


def search_insert_position(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1

        elif nums[mid] > target:
            right = mid - 1
    return right + 1


print(search_insert_position([1, 3, 5, 6], 5))
