# WAP to convert input number of seconds to HH:MM:SS
def timeconvert(a):
    h=a//3600
    k=a%3600
    o=k//60
    i=k%60
    print(h,":",o ,":",i)

u=int(input("Enter number of seconds"))
timeconvert(u)

