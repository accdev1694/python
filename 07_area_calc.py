# we create a calculator the area of a square or rectangle

# collect user input in variables
unit = input("Enter the unit of measurement:")
shape = input("Enter Rectangle or Square:")
length = float(input(f"Enter Length of your {shape}:"))       # type cast to float
breath = float(input(f"Enter Breath of your {shape}:"))       # type cast to float


# calculate area
area = length * breath

# output result to user
print(f"The area of your {shape} is {area}sq{unit}")