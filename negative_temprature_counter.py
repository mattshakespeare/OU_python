#counts the number of days in a week temperature was below 0
#list to store weekly temperatures
weekly_temperatures = [-1,-2,-3,-4,-5,-6,-7]
#intialise a variable to count the number of days
counter = 0 
#iterate through list to find negative tempratures
for temp in weekly_temperatures:
    #create the condition for the counter
    if temp < 0:
        counter += 1
print('The number of negative temperatures in the week was',counter)