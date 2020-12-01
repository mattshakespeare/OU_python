# convert a list a temperatures from celsius to farneheit
#intialise celsius list
celsius = [5,6,7,8,9,10]
#intialise empty farneheit list
farenheit = []
#convert values from celsius to farenheit
for temp in celsius:
    farenheit.append(temp*1.8 + 32)
print(farenheit)