# Q WA function to take dictionary as parameter. Print all keys of the dictionary

def fun1(d :dict):
    return (d.keys())

d1 = {1:"jay",2:"Paras",3:"Piyush",4:"Nilesh","harley davidson":5}

print( list(fun1(d1)) ) 

# [1, 2, 3, 4, 'harley davidson']