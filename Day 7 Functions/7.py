# Q WA function to take a dictionary as parameter. Print value of key "name" 
#   if key "rollno" is having value 100.

def fun1(d :dict):
    for idx, name in d.items():
        if(idx == 100):
            return name

student = {10:"jay",20:"Paras",30:"Piyush",40:"Nilesh",100:"Shaktiman",200:"Boss"}

print( fun1(student) ) 

# o/p : Shaktiman