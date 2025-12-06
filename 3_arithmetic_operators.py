# 3.Arithmetic Operators Task

# Objective
## Read two integers, a and b, from STDIN.
## Print three lines:
### 1. The sum of a and b.
### 2. The difference of a and b (first - second).
### 3. The product of a and b.

# Example
## a = 3
## b = 5

### Output:
#### 8
#### -2
#### 15

# Input Format
## The first line contains the first integer, a.
## The second line contains the second integer, b.

# Constraints
## 1 ≤ a ≤ 10^10
## 1 ≤ b ≤ 10^10

# Output Format
## Print the three results on separate lines:
### a + b
### a - b
### a * b

# Sample Input 0
### 3
### 2

# Sample Output 0
### 5
### 1
### 6

# Explanation
### 3 + 2 = 5
### 3 - 2 = 1
### 3 * 2 = 6

a=int(input())
b=int(input())
sum_=a+b
sub=a-b
product=a*b
print(sum_)
print(sub)
print(product)