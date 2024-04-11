import math

# We will create an application that calculates that area of a circle

# collect radius from user and convert to float
radius = float(input("Type in the radius of the circle:")) 

# collect unit of measurement from user
unit = input("What unit is the radius above?")

# math.pi module  
pi = math.pi    

# area = pi * r^2                                       
area = pi * pow(radius, 2)  

# round to 2 decimal places                            
area = round(area, 2)

# display output to user                                   
print (f"The area of the circle is {area}{unit}")
