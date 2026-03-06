#Coding Challenge 1
n=int(input("\nEnter an integer:"))
count = 0

while n<=0:
   print("invalid number, please try again")
   n=int(input("\nEnter an integer:"))  #inside loop

#now n is valid (n> 0)
print("Factor:", n)
for i in range(1,1+n):
    if n % i == 0:
        count+=1
        print(i)
print("\nTotal factors:", count)

#to avoid infinte loops ask variable again, add varaible again
#can use strings methods but actually need upper and lower and slicing just for project if u dont see restictiosn
# u can use, first three weeks, functions included in exam 2, all points added

# #Coding Challenge 1
#for ending game
# n=int(input("\nEnter an integer:"))
# while n>0:
#     count = 0
#     print("Factor:", n)
#     for i in range(1,n+1):
#         if n%i == 0:
#             count+=1
#             print(i)
#     print("\nTotal factors:", count)
#     n = int(input("\nEnter an integer:"))  # inside loop
#
# print("invalid number, please try again")
#
#
#
#
#
#
#
#
#
#
#
#
#