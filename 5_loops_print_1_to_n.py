# 5.Python Loops Task

# Objective
## Read an integer n from STDIN.
## For all non-negative integers i < n, print i².

# Example
## n = 3
### The list of integers less than 3 is: [0, 1, 2]
### Their squares are:
#### 0
#### 1
#### 4

# Input Format
## A single integer n.

# Constraints
## 1 ≤ n ≤ 20

# Output Format
## Print n lines.
### Each line contains i² for i in the range 0 to n-1.

# Sample Input 0
### 5

# Sample Output 0
### 0
### 1
### 4
### 9
### 16


n = int(input())
for i in range(n):
    print(i * i)