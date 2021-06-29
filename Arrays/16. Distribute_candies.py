'''
Q16. Distribute Candies

Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Sample i/p --> [1,1,2,2,3,3]
Sample o/p --> 3

Sample i/p --> [6,6,6,6]
Sample o/p --> 1

Leetcode --> https://leetcode.com/problems/distribute-candies/

Difficulty --> Easy
'''


def distribute_candies(candyType):
    n = len(candyType)
    can_eat = n/2
    eaten = {}
    candies = 0
    for i in candyType:
        if eaten.get(i) != None:
            continue
        elif candies < can_eat:
            candies += 1
            eaten[i] = True
    return candies


print(distribute_candies([1, 1, 2, 2, 3, 3]))
