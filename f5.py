def altst(s1 :str):
    for n in s1[1::2]:
        print(n,end="")

s = input("Enter a string - ")
altst(s)
