#list of temperatures
temperatures = [32,45,44.2]
#empty list for values above 30
above_30 = []
#iterate through temperature list
for temp in temperatures:
#if value in temperatures is above 30
    if temp > 30:
#append to above_30 list
        above_30.append(temp)
#output all values above 30
print(above_30)
