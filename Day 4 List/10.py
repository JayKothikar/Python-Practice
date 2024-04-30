# 10. Given a Python list, remove all occurrence of 20 from the list
# list1 = [5, 20, 15, 20, 25, 50, 20]
# output:
# [5, 15, 25, 50]
list1 = [5, 20, 15, 20, 25, 50, 20]

print("Before Deleting- ",list1)
# del_elements = list()

for i in range((len(list1)-1),0,-1):
    if list1[i]==20:
        del list1[i]

print("After Deleting - ",list1)

# Before Deleting-  [5, 20, 15, 20, 25, 50, 20]
# After Deleting -  [5, 15, 25, 50]