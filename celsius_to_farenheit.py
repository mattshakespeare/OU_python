# convert a list a temperatures from celsius to farneheit

def celsius_to_farenheit(celsius):
    '''returns farenheit'''
    farenheit = []
    for temp in celsius:
        farenheit.append(temp * 1.8 + 32)
    return farenheit

#intialise celsius list
temps = [5,6,7,8,9,10]
temps = celsius_to_farenheit(temps)
print(temps)
