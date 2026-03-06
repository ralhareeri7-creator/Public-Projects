##################Example 1#####################
"""
Example 1: sum of squares
Prompt for a number n and calculate the sum of squares of all numbers up to N
including N = 1^2 + 2^2 + .....N^2.

for example, if n = 5, sum = 1 + 4 + 9 + 16 + 25 = 55
1^2+2^2+3^2+4^2+5^2
As an example interaction:

Input: 5
Output: 55
"""
#ask for a number
n_int = int(input("\nEnter a number: "))

#calculate sum of squares
#this n_int+1 includes n which is 5 in this case

sum = 0
for i in range(n_int +1):
    sum = sum + i**2
print(sum) #statement is outside