# 10. Given a Python list, remove all occurrence of 20 from the list
# list1 = [5, 20, 15, 20, 25, 50, 20]
# output:
# [5, 15, 25, 50]

list1 = [5, 20, 15, 20, 25, 50, 20]

for i,v in enumerate(list1):
    if v == 20:
        del list1[i]

print(list1)

# [5, 15, 25, 50]