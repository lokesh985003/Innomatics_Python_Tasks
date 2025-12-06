# 4.Python Division Task

# Objective
## Read two integers, a and b, from STDIN.
## Print two lines:
### 1. Integer division result: a // b
### 2. Float division result: a / b

# Description
## No rounding or formatting is required.
## Just print the raw results.

# Example
## a = 3
## b = 5

### Results:
#### Integer division: 3 // 5 = 0
#### Float division: 3 / 5 = 0.6

# Input Format
## The first line contains the integer a.
## The second line contains the integer b.

# Output Format
## Print:
### a // b  
### a / b  

# Sample Input 0
### 4
### 3

# Sample Output 0
### 1
### 1.33333333333


a = int(input())
b = int(input())
print(a // b)
print(a / b)