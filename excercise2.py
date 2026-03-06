num_str = int(input("Input an int: \n"))

count = 0

while num_str != 10:
    count += num_str
    num_str = int(input("Input an int: \n"))
else:
    print(count)