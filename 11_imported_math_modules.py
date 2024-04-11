# you have to import the math module from math class
import math

# ---> math.pi <---
pi = math.pi                  
radius = 1.4
area_of_circle = math.pi * pow(radius, 2)        # pi * r^2
area_of_circle = round(area_of_circle, 2)        # rounded to 2 decimal places
print(area_of_circle)

# ---> math.e <---
print(math.e)           # constant e

# ---> math.sqrt <---
square_root_of_36 = math.sqrt(36)
print(square_root_of_36)

# ---> math.ceil <---
# this rounds a float number up
radius = 2.333445
print(math.ceil(radius))

# ---> math.floor <---
# this rounds a float number down
print(math.floor(radius))