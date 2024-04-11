# There are math functions that come built-in into python
 
# ---> round function <---
# rounds a float to a defined number of decimal places
length = 12.55
breath = 2.45
area = round(length * breath, 1)         
# the round function takes two parameters, the variable and the decimal places
# and seperated by a coma
print(area)                 # gives 30.7
# you could also round to nearest integer by not adding any decimal place parameter
area = round(length * breath)
print(area)                 # gives 31


# ---> absolute value <---
# this is the distance away from 0 as a whole number
temperature = -5
print(abs(temperature))     # gives 5

# --> power function <---
# it takes two parameters, the base, and the exponent, seperated by a coma
power_of_five = pow(5, 2)
print(power_of_five)

# ---> max function <---
# used to find the maximum value 
print(max(length, breath))   # gives 12.55, for length

# ---> min function <---
# finds the minimum value 
print(min(length, breath))  # gives 2.45, for breath  