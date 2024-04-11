# Conditional Statements
# If, Else, else is statements are known as conditionals

# ---> if statements <---
# lets write a program to check the color red in a flag

# collect user input and convert to uppercase
color = (input("is there color red in the flag? Y/N/Meh:")).capitalize()

# if statement
if color == "Y":
    print("You are correct, there is Red")
    
# else if (elif) statement
elif color == "Meh":
    print("You are lucky")
    
# else statement
else:
    print("You are so wrong")

