# LeetCode 1431: Kids With the Greatest Number of Candies

# Problem
## You are given:
### - An integer array candies
### - An integer extraCandies

## candies[i] = number of candies the i-th kid has.

## Return a boolean array result of length n, where:
### result[i] = true  
#### if after giving the i-th kid all extraCandies,  
#### they have the greatest number of candies among all kids,
### else result[i] = false.

# Notes
## Multiple kids can have the greatest number of candies.

# Example 1
## Input:
### candies = [2,3,5,1,3], extraCandies = 3
## Output:
### [true, true, true, false, true]
## Explanation:
### Kid 1 → 2 + 3 = 5  
### Kid 2 → 3 + 3 = 6  
### Kid 3 → 5 + 3 = 8  
### Kid 4 → 1 + 3 = 4  
### Kid 5 → 3 + 3 = 6  
### Max original candies = 5  
### So kids 1,2,3,5 become ≥ 5 → true

# Example 2
## Input:
### candies = [4,2,1,1,2], extraCandies = 1
## Output:
### [true, false, false, false, false]

# Example 3
## Input:
### candies = [12,1,12], extraCandies = 10
## Output:
### [true, false, true]

# Constraints
## n == candies.length
## 2 <= n <= 100
## 1 <= candies[i] <= 100
## 1 <= extraCandies <= 50


class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)
        result = []
        for i in candies:
            result.append(i + extraCandies >= greatest)
        return result