# Problem: convert miles to kilometers 

# Input a possibly empty list of distances in miles
distance_in_miles = [1,13,10,4]

# Output: the list of distances in kilometers
distance_in_km = []

# Iterate through list
for distance in distance_in_miles:
    # covert each value from miles to kilometers  
    # Round each value to 1.d.p
    distance_in_km.append(round(distance * 1.61, 1))

# Output: list of distances in kilometers
print(distance_in_miles)
print(distance_in_km)
