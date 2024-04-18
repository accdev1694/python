# This program will collect 5 loved movie names from the user 
# and print it to the console.

# collect users best movie
movie = input("Enter your best most loved movie: ")
# initialize a movie count variable to 0
count = []

# loop continues to ask user for movies 4 more times
while range(len(count), 5):                                 # if the the movies in the count variable is less than 5, 
    count.append(movie)                                     # add the movie to count list
    movie = input("Enter another loved movie: ")            # keep asking user for loved movies
    
print(f"out of your {len(count)} most loved movies, your most loved movie is 1.) {count[0]}, then 2.) {count[1]}, 3.) {count[2]}, 4.) {count[3]}, 5.) {count[4]}")       # break the loop after 6th count and print
    
    
    