'''
Q2. Sum of all subarrays

subarrays --> contagious (nC2 + n)
sample i/p --> [1,2,2]
sample o/p --> [1,3,5,2,4,2]

difficulty --> novice
'''


def sum_of_sub_arrays(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i:j+1])
            answer.append(sum(arr[i:j+1]))
    return answer


print(sum_of_sub_arrays([1, 2, 2]))
