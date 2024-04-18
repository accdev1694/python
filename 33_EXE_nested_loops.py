# nested Loops
# we create a 12 times table

# iterate through the range of numbers from 1 to 12
for multiplier in range(1,13):                                                      
    for multiplicand in range(1,13):                                            # nest the multiplicand iteration of range 1 to 12
        print(f"{multiplier} x {multiplicand} = {multiplier * multiplicand}\n") # perform the calculation of multiplying both numbers

print(" ")  
print("------------------------------------------")      
print("THE END!")
    