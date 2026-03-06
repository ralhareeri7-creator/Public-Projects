n_str = input("\n:~Input an integer (0 terminates)~:")
n_int = int(n_str)
# Good stuff goes here
even_count=0
even_sum=0
odd_count=0
odd_sum=0

while n_int != 0:
    #do something
    if n_int>0:
        if n_int%2==0:
            even_count+=1
            even_sum+=n_int
        else:
            odd_count +=1
            odd_sum+=n_int
    n_str = input("\n:~Input an integer (0 terminates)~:")
    n_int=int(n_str)

positive_int_count=even_count+odd_count


#Do not change the following lines of code
print("\n")
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)
