# 4. Print two lists in the following order
# list1 = [5, 6,7]
# list2 = [0, 1]
# output:
# 50,51,60,61,70,71

list1 = [5, 6,7]
list2 = [0, 1]


for i,p in enumerate(list1):
    for j,q in enumerate(list2):

        # for last char to not have a coma 
        if((i==len(list1)-1) and (j==len(list2)-1)):
            print(f"{p}{q}",end="")
            continue
        
        print(f"{p}{q},",end="")
            
