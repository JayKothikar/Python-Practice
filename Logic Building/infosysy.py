
def checkexp(s:str):
    
    flag=1
    for i in range(0,len(s),1):
    
        if(s[i]=='('):
          print(s[i])
          o=i+1
          while(o<len(s)):
             if(s[o]==')'):
                print(s[o])
                flag=1
                break
             else:
                flag=0
             o=o+1
    if(flag==1):
       print("Right mathematical expression")
    else:
       print("Wrong input")       

u=input("Enter maths equation") 
checkexp(u)
             
