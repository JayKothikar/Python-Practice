# 11. Take a number as input from the user. 
# Print maximum and minimum integer which can 
# be generated using all the digits in the input number

user_in = input("Enter a number - ")

list_in = list()
for l in user_in:
    list_in.append(l)

list_in.sort()
small_num = "".join(list_in)

list_in.sort(reverse=True)
big_num = "".join(list_in)

print("Biggest Num  ",big_num)
print("Smallest Num ",small_num)

# Enter a number - 9500241
# Biggest Num   9542100
# Smallest Num  0012459