# we will create an app that converts weight from pounds to kg and vice versa

# get user input and capitalize it
unit_from = input("What are you converting from? (Kg/Lbs) ").capitalize()
unit_to = input("What are you converting to? (Kg/Lbs) ").capitalize()

# collect weight
weight = float(input("Type in the weight to convert: "))

# conditionals
if unit_from == "Lbs":
    print(f"Your weight is: {round(weight * 0.453592, 1)} {unit_to}")
    
elif unit_from == "Kg":
    print(f"Your weight is: {round(weight * 2.20462, 1)} {unit_to}")
    
else:
    print(f"{unit_from} is not valid! Type a valid response")
             