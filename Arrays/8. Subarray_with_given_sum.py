'''
Q8. Subarray with given sum

Given an unsorted array A of size N of non-negative integers, find a continuous
subarray which adds to a given number S.
return the start and end index of the array

Sample i/p --> nums = [1,2,3,7,5]
sample o/p --> [1,3]
Difficulty --> Easy
'''


# def subarray_with_given_sum(nums, target_sum):
#     left = 0
#     right = 1
#     curr_sum = nums[left]
#     while right < len(nums):
#         curr_sum += nums[right]
#         if curr_sum == target_sum:
#             return [left, right]
#         elif curr_sum > target_sum:
#             left += 1
#             right = left+1
#             curr_sum = nums[left]
#         else:
#             right += 1
#     return -1

def subarray_with_given_sum(nums, target_sum):
    left = 0
    right = 0
    curr_sum = nums[left]
    while right < len(nums):
        if curr_sum == target_sum:
            return [left, right]

        if curr_sum > target_sum:
            curr_sum -= nums[left]
            left += 1

        if curr_sum < target_sum:
            right += 1
            curr_sum += nums[right]

    return -1


print(subarray_with_given_sum([1, 2, 3, 7, 5], 12))
