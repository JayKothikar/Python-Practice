# Q WA function to take list of strings as parameter and print all strings 
#   which have character 's' 2 times

def ss_twice(list_in :list):
    list_of_2s = list()
    cnt_s = 0
    for name in list_in:

        for letter in name:
            if cnt_s == 2:
                list_of_2s.append(name)
                cnt_s = 0
                break
            if (letter.lower() == "s"):
                cnt_s += 1
        cnt_s = 0

    return list_of_2s

names = ["Sakitman","Shardul","Sushant","Shivam","Safushan","Assatha"]

out = ss_twice(names)
print(out)

# ['Sushant', 'Safushan', 'Assatha']