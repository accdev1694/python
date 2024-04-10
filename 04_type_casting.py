# Type Casting
# this is basically data type conversion

# ---> Explicit Conversion
# Conversion by the programmer
quantity = 10
print(type(quantity))           # check type (currently int)

# conversions
quantity = str(quantity)        # convert to string
print(type(quantity))           # now type of str
print(quantity)                 # check value (now "10")

quantity = float(quantity)      # convert to foat
print(type(quantity))           # now type of float
print(quantity)                 # check value (now 10.0)

quantity = bool(quantity)       # convert to boolean
print(type(quantity))           # now type of boolean
print(quantity)                 # check value (now true)

# You can convert between different data types

# ---> Implicit conversion
# means conversion by the program

# use case 1: arithmetics on integers and floats
a = 5                           # integer
b = 3.2                         # float
a = a / b                       # arithmetics
print(a)                        # 1.5625
print(type(a))                  # type of float (originally and integer)

# use case 2: user input
age = input("what is your age") # collect user age
print(type(age))                # age outputs as string from user input




