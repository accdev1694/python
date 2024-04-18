# Countdown Timers in Python

# import the time module
import time                         

# a timer to create a file after 10 seconds
with open("love_you.html", "w") as file:        # use the open function to write a file(2nd parameter), with file name and extension(first parameter)
    time.sleep(10)                              # time delay for 10 seconds
    file.write("i love you babe!!!")            # writes or creates the file with some content
    


    
