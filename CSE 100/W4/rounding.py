cars = 3
people = 8

people_per_car = people / cars

# Round to 1 decimal
print(f"There are {people_per_car:.1f} people in each car.")
# Output: There are 2.7 people in each car.

# Round to 2 decimals
print(f"There are {people_per_car:.2f} people in each car.")
# Output: There are 2.67 people in each car.

# Round to 3 decimals
print(f"There are {people_per_car:.3f} people in each car.")
# Output: There are 2.667 people in each car.

distance = 9 * 1205 * 18

# Scientific notation with 3 digits of precision
print(f"The distance is: {distance:.3e} meters.")
# Output: The distance is: 1.952e+05 meters.

# Scientific notation with 6 digits of precision
print(f"The distance is: {distance:.6e} meters.")
# Output: The distance is: 1.952100e+05 meters.

big_number = 123456789

# Display without formatting:
print(f"The number is: {big_number}")
# Output: The number is: 123456789

# Display with "," formatting:
print(f"The number is: {big_number:,}")
# Output: The number is: 123,456,789

# Display with "_" formatting:
print(f"The number is: {big_number:_}")
# Output: The number is: 123_456_789

import math

radius = 5
area = math.pi * (radius ** 2)
print(f"The area is: {area}")
# Output: The area is: 78.53981633974483

# math.ceil(value)—Rounds value up to the next whole number, the "ceiling."

# math.floor(value)—Rounds value down to the next whole number.

# math.exp(value)—Raises e to the power of value.

# math.sin(value)—Computes the trigonometry sine function of value in radians.

import math

weight = 1.65

lower = math.floor(weight)
print(lower)
# Output: 1

higher = math.ceil(weight)
print(higher)
# Output: 2