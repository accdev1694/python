# In this 3rd type of conditionals, we will check if a user typed in their name

# get user name
user_name = input("Type in your name:")

# check if field is empty
if user_name == "":
    print("Please type in your name")

# ensure user only type in alphabets, then print name
elif user_name.isalpha():
    print(f"Your Name is {user_name}")
    
# ensure nothing else asides alphabets are typed
else:
    print("Type only alphabets")   