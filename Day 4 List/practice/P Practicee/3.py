# 3. Given a Python list of numbers. Turn every item of a list into its square root
# aList = [1, 4, 9, 16, 25, 36, 49] 
# output:
# [1, 2, 3, 4, 5, 6, 7]

aList = [1, 4, 9, 16, 25, 36, 49] 
print(aList)

for i,v in enumerate(aList):
    aList[i]=v**2

print(aList)
