l = [[2,3],(9,67),[56,67],(100,299),[1,4]]
unique_pairs = set()
max_mult = 0 
max_pair = l[0]
for pair in 1:
    # if pair not in unique_pairs:
    if pair not in unique_pairs:
        m = pair[0] * pair[1]
        if m >max_mult:
            max_mult = m
            max_pair = pair
print(max_pair)