'''
Q3. Longest continues subarray

An arithmetic array is an array that contains at least two integers and the
differences between consecutive integers are equal. For example, [9, 10], [3, 3, 3],
and [9, 7, 5, 3] are arithmetic arrays, while [1, 3, 3, 7], [2, 1, 2], and [1, 2, 4] are
not arithmetic arrays.
Sarasvati has an array of N non-negative integers. The i-th integer of the array is
Ai
. She wants to choose a contiguous arithmetic subarray from her array that has
the maximum length. Please help her to determine the length of the longest
contiguous arithmetic subarray.
Input
The first line of the input gives the number of test cases, T. T test cases follow.
Each test case begins with a line containing the integer N. The second line
contains N integers. The i-th integer is Ai
.

Output
For each test case, output one line containing Case #x: y, where x is the test case
number (starting from 1) and y is the length of the longest contiguous arithmetic
subarray.

sample i/p --> [10,7,4,6,8,10,11]
sample o/p --> [4,6,8,10]--> 4

Difficulty --> Easy
'''


def longest_arr(arr):
    left = 0
    right = 1
    max_ = 0
    len_ = 2
    ap_diff = float('-inf')

    while right <= len(arr)-1:
        diff = arr[right] - arr[left]
        if diff == ap_diff:
            len_ += 1
        else:
            ap_diff = diff
            max_ = max(max_, len_)
            len_ = 2
        right += 1
        left += 1

    return max_


print(longest_arr([1, 2, 0, 7]))
