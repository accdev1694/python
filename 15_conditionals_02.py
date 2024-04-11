# Here we will write code to check the score of an exam

# get user score and convert to float
score = float(input("Enter your test score:"))

# start with the highest and work your way down

# check if score is above maximum allowable number
if score > 100:                                             
    print("Invalid. Enter a number between 0 and 100")

# check if score is between 70 and 100    
elif score >= 70:                                           
    print("You scored an A, Congrats")


# check if score is between 60 and 69
elif score >= 60:
    print("You scored a B, not bad")


# check if score is between 50 and 59
elif score >= 50:
    print("you scored a C, try harder")

# check if score is between 40 and 49
elif score >= 40:
    print("You scored a D, not good")

# check if score is between 35 and 39
elif score >= 35:
    print("You scored an E, Horrible")

# check if score is 34 and under
else:
    print("You Failed!!!")