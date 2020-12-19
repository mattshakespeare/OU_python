#Input: list of whole numbers
input_list = []

#Output: None if No values exceed 100
value = None

# Itreate through list of numbers
for num in input_list:

    #if value in list exceeds 100
    if num > 100:
        #Output: value that exceeds 100
        value = num
        #Break loop if value exceeds 100
        break

#Output: None if no values exceed 100 OR Output: first value found that exceeds 100
print(value)
