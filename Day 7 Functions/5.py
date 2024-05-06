# Q WA function to take a string as parameter. 
#   Print its alternate characters starting from 2nd character

user_in = input("Enter a string - ")

def fun_alt_str(string_1):
    alt_str = str()
    for n in range(0,len(user_in)-1,2):
        alt_str += "".join(string_1[n+1])
    return alt_str

alt_str = fun_alt_str(user_in)
print(alt_str)

# Enter a string - hhooww  aarree  yyoouu  ddooiinngg..
# how are you doing.