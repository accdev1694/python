# import the time module
import time


# collect user input of time
timer = int(input("Enter time: "))
# iterate through time input and print
for t in reversed(range(timer)):                # reverse the count
    sec = t % 60                                # create seconds
    min = int(t / 60) % 60                      # create minutes
    hr = int(t / 3600)                          # create hours
    print(f"{hr:02}:{min:02}:{sec:02}")         # print the time
    time.sleep(1)                               # delay 1 second between each loop
    
print("Blast Off!!!")                           # escape the loop after countdown completes