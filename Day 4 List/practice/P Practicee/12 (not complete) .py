# 12. Take integer from user and print all odd numbers which can be generated using any number of digits from given number
# Ex. 
# Input: 3421  o/p: 1,3,13,43,23,31,41,21,421,241,341,431,423,243,143,413,1243,1423,4213,4123, 2413,2143, .. etc

user_in = input("Enter a number - ")
u_deci = int(input("Enter what decimal value number should be generated  - "))

# digit will get the unique value in a set that set will be converted into a list
digit = set()
for v in user_in:
    digit.add(int(v))
print(digit,type(digit))
digit=list(digit)
sorted(digit)

print(digit,type(digit))
ot = list()

deci = 0

for i,v in enumerate(digit):
    ot.append(v)
for v in digit:
    ot.append(int(str(v)+str(v+1)))
print(ot,end="")