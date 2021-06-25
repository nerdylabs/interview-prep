'''
Q6. Max area of water

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Leetcode --> https://leetcode.com/problems/container-with-most-water/

sample i/p --> height = [1,8,6,2,5,4,8,3,7]
sample o/p --> 49

Difficulty --> Medium
'''


def max_area_of_water(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right-left)
        max_area = max(area, max_area)
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_area


print(max_area_of_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
