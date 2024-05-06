# 8. Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look like the following list

# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# Sub List to be added = ["h", "i", "j"]
# output:
# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n'] 

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list= ["h", "i", "j"]

def find_in_list(list :list):
    for i, v in enumerate(list):
        if(v == "g"):
            # list.append(7000)
            # print("Find it")
            list.append(sub_list)
            
        if( str(type(v)) == "<class 'list'>" ):
            list = list[i]
            find_in_list(list)
            continue
        # print(v)

find_in_list(list1)
print(list1)