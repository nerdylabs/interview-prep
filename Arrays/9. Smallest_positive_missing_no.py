'''
Q9. Smallest positive missing number

Find the smallest positive missing number in the given array.

sample i/p --> [0, -10, 1, 3, -20]
sample o.p --> 2
Difficulty --> Easy
'''


def smallest_positive_missing_no(nums):
    seen = [False for i in range(len(nums))]
    for i in range(len(nums)):
        if nums[i] >= 0:
            seen[nums[i]] = True
    for j in range(len(nums)):
        if not seen[j]:
            return j


print(smallest_positive_missing_no([0, -10, 1, 3, -20]))
