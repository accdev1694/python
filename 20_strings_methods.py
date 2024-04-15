# a string is a series of text or characters

# Useful String Methods

    # 01: ---> Length (len) <---
# the len() method gets the length of a string
# lets get a user input
course = input("what is your course of study?")

response = len(course)

print(response)          # (architecture), gives 12

# the program counts spaces as well. Try  a character with spaces

    # 02: ---> find() method <---
# this method finds the first position of any character in a string
# finds the first occurance of a space
position = course.find(" ")        
print(position)

    # 03: ---> last occurance rfind() or reverse-find <---
last_occurance = course.rfind("t")
print(last_occurance)

# if its not able to locate any character, it returns -1

    # 04: ---> capitalize <---
# capitalizes the first letter in a string
caps = course.capitalize()
print(caps)

    # 05: ---> title <---
# capitalizes all the first letters of each word in a string
titl = course.title()
print(titl)

    # 06: ---> upper <---
# capitalizes all the characters in a string
upr = course.upper()
print(upr)

    # 07: ---> lower <---
# make lower case
low = course.lower()
print(low)

    # 08: ---> isdigit() method <---
# returns true if the caharacters are all digits or numbers, no mix
# returns false if the aharacters contain both digits and anything else, 
# even spaces or special characters
num = course.isdigit()
print(num)

    # 09: ---> isalpha() method <---
# returns true if the characters are all alphabets, no mix
alph = course.isalpha()
print(alph)

    # 10: ---> count() method <---
# counts the number of occurance of a character
print(course.count("-"))

    # 11: ---> replace() method <---
# replaces a character with some other character, 
# it takes two arguments, seperated with comas
repl = course.replace("-", "/")
print(repl)

    # 12: ---> help function <---
# display all the available string methods
print(help(str))
# enter to see more
