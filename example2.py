################Example 2###################
"""
Example 2: Largest number
Ask the user to enter valid numbers until the user enters 0.
A valid number is between -200 and 200, inclusive.
Then, find and print the largest number entered.
As an example to understand the topic:

Input a number:4
Input a number:5
Input a number:250
Error. Invalid number
Input a number:100
Input a number:2
Input a number:1
Input a number:0
100
"""
n_int=int(input("\nEnter a number: "))
max_int= -201 #-10**6
while n_int !=0:
    if -200<=n_int<=200:
        if n_int > max_int:
            max_int = n_int
    else:
        print("Error. not  Invalid number")

    n_int = int(input("\nEnter a number: "))
print(max_int)