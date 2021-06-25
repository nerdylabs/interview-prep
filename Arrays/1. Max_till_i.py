'''
Q1. Max till i

Given an array calculate the max value till the ith postion
sample i/p -->[1,0,5,4,6,8]
smaple o/p -->[1,1,5,5,6,8]

difficulty --> novice
'''


def max_till_i(arr):
    max_ = arr[0]
    answer = []
    for i in arr:
        max_ = max(max_, i)
        answer.append(max_)
    return answer


print(max_till_i([1, 0, 5, 4, 6, 8]))
