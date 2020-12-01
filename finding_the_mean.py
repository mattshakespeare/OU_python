#find the mean
#intialise a list of numbers
numbers = [1,2]
#intialise aggregate to sum values
aggregate = 0
#intialise count to measure the length of the list
count = 0
#iterate through list and calculate the length of the list and sum of the values
for number in numbers:
    count += 1
    aggregate += number
#calculate the mean
mean = aggregate/count
#output mean
print('The mean of the list of numbers is', mean)