# 6.Leap Year Function Task

# Objective
## Determine whether a given year is a leap year.
## If it is a leap year, return True.
## Otherwise, return False.

# Rules (Gregorian Calendar)
## A year is a leap year if:
### 1. It is evenly divisible by 4
#### EXCEPT when it is divisible by 100
##### UNLESS it is also divisible by 400

# Meaning:
## ✔ Years like 2000, 2400 are leap years.
## ✘ Years like 1800, 1900, 2100, 2200, 2300, 2500 are NOT leap years.

# Task
## Complete the function is_leap(year):
### Return True if the year is a leap year.
### Otherwise, return False.

# Input Format
## A single integer:
### year — the year to test.

# Constraints
## 1900 ≤ year ≤ 10⁵

# Output Format
## The function must return a Boolean value:
### True
### or
### False

# Sample Input 0
### 1990

# Sample Output 0
### False

# Explanation
### 1990 is not divisible by 4 → Not a leap year.


year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(True)
else:
    print(False)