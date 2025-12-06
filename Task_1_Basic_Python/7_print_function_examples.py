# 7.Print Function Task

# Objective
## Read an integer n from STDIN.
## Without using string methods, print the numbers:
### 1 2 3 ... n
## As a single string with no spaces.

# Example
## n = 5
### Output string: 12345

# Input Format
## A single integer n.

# Constraints
## 1 ≤ n ≤ 150

# Output Format
## Print the list of integers from 1 to n as a single string.
### No spaces
### No separators

# Sample Input 0
### 3

# Sample Output 0
### 123


n = int(input())
for i in range(1, n + 1):
    print(i, end="")