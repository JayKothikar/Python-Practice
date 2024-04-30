# Q Given list of employees. This list may contain repetitions.  
#   Find all unique employee names and print them as per order 
#   of second character in that name. Use lambda function and 
#   normal function both.

list_of_s = ["Today","is","a","day","day","to","play","soccer"]

vy = (lambda list_of_s:set(list_of_s))
print(vy(list_of_s))

