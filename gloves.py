gloves = [10,8,3,5]

total = gloves[0] + gloves[1] + gloves[2] + gloves[3]

print(total)

total = 0

for i in range(0, len(gloves)):
    total += gloves[i]

print(total)

total = 0

for i in range(len(gloves)):
    total += gloves[i]

print(total)

temp = gloves[0]
gloves[0] = gloves[3]
gloves[3] = temp
temp = gloves[1]
gloves[1] = gloves[2]
gloves[2] = temp
print(gloves)
    
