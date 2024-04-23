def dictfu(s :str):
    for key, value in s.items():
        if value == 100:
            print("Key associated with value 100:", key)
            return key
# ------------------------

stud = {"rahul":100,"pawan":200,"ravan":300,"shranavan":400,"rahul":500}

print(stud)
print(dictfu(stud))