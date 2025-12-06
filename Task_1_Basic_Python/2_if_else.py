# 2.Python If-Else Task

# Objective  
## Print **Weird** if the number is weird. Otherwise, print **Not Weird**.

# Rules  
## A number is considered *Weird* if:  
### The number is **odd**,  
### OR the number is **even** and **in the range 6 to 20** (inclusive).

## A number is **Not Weird** if:  
### It is **even** and **in the range 2 to 5** (inclusive),  
### OR it is **even** and **greater than 20**.

# Input Format  
## A single integer **n**.

# Constraints  
### 1 ≤ n ≤ 100

# Output Format  
## Print **Weird** or **Not Weird** based on the conditions.

# Sample Input 0  
### 3

# Sample Output 0  
### Weird

# Sample Input 1  
### 24

# Sample Output 1  
### Not Weird

n = int(input())

if n % 2 != 0:
    print("Weird")
elif n >= 2 and n <= 5:
    print("Not Weird")
elif n >= 6 and n <= 20:
    print("Weird")
else:
    print("Not Weird")