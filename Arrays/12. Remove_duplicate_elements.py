'''
Q. 12 Remove Duplicate elements from sorted array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.


Leetcode --> https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Sample i/p --> [1,1,2]
sample o/p --> [1,2]

Difficulty --> Easy
'''


def remove_duplicates_from_sorted_array(nums):
    if len(nums) == 0:
        return 0
    seen = nums[0]
    k = 0
    i = 1
    while i < len(nums):
        if seen == nums[i]:
            k += 1
            nums.remove(nums[i])
        else:
            seen = nums[i]
            i += 1
    return len(nums)


print(remove_duplicates_from_sorted_array([1, 1, 2]))
