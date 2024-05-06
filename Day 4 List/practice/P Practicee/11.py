# 11. Take a number as input from user. 
# Print maximum and minimum integer which can be generated using all the digits in the input number
# Ex. Input 3421   : o/p max: 4321, min 1234
# Input 7789    : o/p max: 9776   min 6779


user_in = input("Enter a number - ")

l = list(user_in)
min_v = "".join(sorted(l))
max_v = "".join(sorted(l,reverse=True))


print("max:",max_v,",","min",min_v)

#  o/p max: 4321, min 1234s
