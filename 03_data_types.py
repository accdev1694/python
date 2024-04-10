# Data Types

# ---> 01: Integers
# Integers are whole numbers
age = 2
quantity = 10

# lets combine them
print(f"the lions are {age} years old and they are {quantity} in number")

# ---> 02: Floats
# Floats are numbers with decimals
distance = 2.5
minutes = 1.23

# lets combine them
print(f"I ran for {distance} km, for {minutes} min")

# ---> 03: Strings
# strings are a series of characters or text 
name = "Oloche"
location = "Coventry"
address = "21 camel close"
# strings are enclosed within quotes

# lets combine them
print(f"my name is {name}, i live in {location} and my address is '{address}'")

# ---> 04 Booleans
# Booleans are statements or expressions that evaluate to true or false
# Boolans are typically used within if statements to validate states
happy = True
coming = False
print(f"Everyone Happy: {happy}")
print(f"Are you coming: {coming}")

# Typical use case:
if coming:
    print("I am coming")
else:
    print("Not coming")
    
# another use case:
if happy:
    print("clap clap clap")
else:
    print("stay silent")
    
# Booleans are not written within quotes and the first letter is a capital

# Multiple assasgnment of variables
#lets assign these variables seperately
color = "blue"
shape = "triangle"
size = 20

# now lets printe them seperately
print(color)
print(shape)
print(size)


# now lets assign them in multiples
colors, shapes, sizes = "greens", "squares", 200

# lets print them
print(colors, shapes, sizes)

# you can also set multiple variables to the same value
a = b = c = 20

# now lets print them
print(a, b, c)


