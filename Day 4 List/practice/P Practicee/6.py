# 6. Remove empty strings from the list of strings
# list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
# output:
# ["Ashish", "Atharva", "Amit", "Revati"]

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]

for i, v in enumerate(list1):
    if v == "":
        del list1[i]

print(list1)

# ["Ashish", "Atharva", "Amit", "Revati"]