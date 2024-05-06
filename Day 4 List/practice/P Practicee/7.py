# 7. Add item 7000 after 6000 in the following Python List
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def find_in_list(list :list):
    for i, v in enumerate(list):
        if(v == 6000):
            list.append(7000)
        if( str(type(v)) == "<class 'list'>" ):
            list = list[i]
            find_in_list(list)
            continue
        # print(v)

print("Before - ",list1)
print("")
find_in_list(list1)
print("After  - ",list1)
print("")

# Before -  [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# After  -  [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]