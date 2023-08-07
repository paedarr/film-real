import numpy as np
import csv

csv_file_path = 'HollywoodMovies.csv'

movie_database = {}

with open(csv_file_path, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        movie_name = row["name"]
        movie_rating = int(row["rating"])
        movie_budget = int(row["budget"])
        movie_director = row["director"]
        
        movie_info = {
            "name": movie_name,
            "rating": movie_rating,
            "budget": movie_budget,
            "director": movie_director,
        }
        
isActive = False
#isActive is for the main program runtime
while isActive == True:
    #have a ui for this in the future, but ask if user is an existing user
    
    ##--IS USER EXISTING USER SECTION--##
    existingUser = False
    does_user_exist = str(input("Are you an existing user? y/n:"))
    if does_user_exist == "y":
        existingUser = True
    elif does_user_exist == "n":
        existingUser = False
    else:
        print("Unknown input...exiting program")
        break
    ##---------------------------------##
    
    if existingUser == True:
        #have user access username+password database for a login
        user_username_entry = str(input("Please enter your username"))
        user_password_entry = str(input("Please enter your password:"))
    elif existingUser == False:
        user_new_username_entry = str(input("Please enter your new username:"))
        user_new_password_entry = str(input("Please enter your new password:"))
    
        
movie_database[movie_name] = movie_info
        
        
sorted_movies = sorted(movie_database.items(), key=lambda x: x[0])