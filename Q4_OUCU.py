## check if any of the three numbers is the product of the others.
#intialise variable a: integer between 1-100
a = 3
#intialise variable b: integer between 1-100
b = 2
#intialise variable c: integer between 1-100
c = 6
#Output answer as a string
if a == b*c:
    answer = 'a = b*c'
elif b == a*c:
    answer = 'b = a*c'
elif c == b*a:
    answer = 'c = a*b'
else:
    answer = 'No number is product of others'
#Output answer
print(answer)
