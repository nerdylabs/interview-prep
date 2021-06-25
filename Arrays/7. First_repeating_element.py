'''
Q7. First Repeating Element

Given an array arr[] of size N. The task is to find the first repeating element in an
array of integers, i.e., an element that occurs more than once and whose index of
first occurrence is smallest.

Sample i/p --> [1,5,3,4,3,5,6]
sample o/p --> 1

Difficulty --> Easy
'''


def first_repeating_element(arr):
    seen = {}
    min_ = float('inf')
    for i in range(len(arr)):
        if seen.get(arr[i]) != None:
            min_ = min(min_, seen[arr[i]])
        else:
            seen[arr[i]] = i
    return -1 if min_ == float('inf') else min_


print(first_repeating_element([1, 5, 3, 4, 3, 5, 6]))
