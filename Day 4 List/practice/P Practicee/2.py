# 2. take a list 'l1' of even nos between 150 to 250. Print its length.
# Then create another list 'l2' using 'l1', containing only nos divisible by 4 from 'l1'.

l1 = list()
l2 = list()

for i in range(150,251,2):
    l1.append(i)

print(l1)
print(len(l1))

for i in l1:
    if( i % 4 == 0):
        l2.append(i)

print(l2)


# [150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250]
# 51
# [152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236, 240, 244, 248]