# WAP that accepts three integers from the user and return true 
# if two or more of them (integers )
#  have the same rightmost digit. The integers are non-negative
def truecheck(a,b,c):
     i=a%10
     j=b%10
     k=c%10
     if(i==j or j==k or i==k):
          return True
     else:
          return False

    


print("Enter three number to check are there atleast two number have same rightmost digit")
k=int(input("First:"))
o=int(input("Second:"))
l=int(input("Third:"))
print(truecheck(k,o,l))