
# For Loops are used to iterate over a fixed number of times
# iterate over lists, ranges, strings, sequences, etc

# 01: ---> count to 6 <---
for i in range(1, 7):           # the last number is exclusive, so use 7 if you want to count to 6
    print(i)
    
print(" ")    
print("------")
print(" ")
    
# 02: ---> lets reverse the count <---
for x in range(6, 0, -1):       # starts from 6 to 1, last number is exclusive again so use 0. -1 tells it to reverse
    print(x)
    
print(" ")    
print("------")
print(" ")

# 03: ---> Or (print numbers from 4 to 9) <---
# to reverse your count, wrap your range in a reversed function
for y in reversed(range(4, 10)):
    print(y)

print(" ")    
print("------")
print(" ")   
    
# 04: ---> add steps to your count <---
# print even numbers between 1 and 10
for even_num in range(2, 11, 2):    # last number is always excluded so add 1
    print(even_num)
    
print(" ")    
print("------")
print(" ")

# 04: ---> iterate over a string <---
# print some text along with the characters of the string
love = "LOVE"
for char in love:
    print(f"{char} is in the word {love}")
    
print(" ")    
print("------")
print(" ")

# 05: ---> Iterate over a string 2 <---
# we will create the meaning of an accronyn "LOVE"

love = "LOVE"
meaning = ["Life", "Of", "vast", "Empathy"]

for char in range(len(love)):
    print(f"{love[char]}: {meaning[char]}")
    


    

        
