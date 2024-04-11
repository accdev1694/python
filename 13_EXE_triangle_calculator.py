import math

# Here we will create an application that calculates the hypothenuse of a triangle

# lets collect user data
base = float(input("what is the base of your triangle:"))
height = float(input("what is the height of your triangle:"))
unit = input("what unit is are the dimensions above:")

# calculate the hypotenuse
hypotenuse = math.hypot(base, height)

# shorten the decimal places to 2
hypotenuse = round(hypotenuse, 2)

print(f"The Hypotenuse is: {hypotenuse}{unit}")


