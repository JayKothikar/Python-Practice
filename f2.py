l1 = [11,7,42,22,2,44,121,55,66,84,77,88]

def de11(ll):
    ct=0
    for num in ll:
        if (num%11==0):
            print(ll[ct])
        ct+=1

de11(l1)
