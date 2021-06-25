'''
Q4. Record breaking day

Isyana is given the number of visitors at her local theme park on N consecutive
days. The number of visitors on the i-th day is Vi

. A day is record breaking if it

satisfies both of the following conditions:
● The number of visitors on the day is strictly larger than the number of
visitors on each of the previous days.
● Either it is the last day, or the number of visitors on the day is strictly larger
than the number of visitors on the following day.
Note that the very first day could be a record breaking day!
Please help Isyana find out the number of record breaking days.

sample i/p--> [1,2,0,7,2,0,2,2]
sample o/p--> 2
difficulty --> Easy
'''


def record_breaking_day(arr):
    max_so_far = 0
    count = 0
    for i in range(len(arr)-1):
        if arr[i] > max_so_far and arr[i] > arr[i+1]:
            count += 1
            max_so_far = arr[i]
    if arr[i+1] > max_so_far:
        count += 1
    return count


print(record_breaking_day([1, 2, 0, 7, 2, 0, 2, 2]))
