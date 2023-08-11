import numpy as np
import csv
import cryptography
from cryptography.fernet import Fernet

from adjustInfo import readKeys
from adjustInfo import readPasswords
from adjustInfo import writeKeys
from adjustInfo import writePasswords

csv_file_path = 'HollywoodMovies.csv'

movie_database = {}

with open(csv_file_path, newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        movie_name = row["Movie"]
        movie_audience_score = row["AudienceScore"]
        movie_budget = row["Budget"]
        movie_genre = row["Genre"]
        movie_studio = row["LeadStudio"]
        movie_rottenTomato_score = row["RottenTomatoes"]
        movie_story = row["Story"]
        
        movie_info = {
            "Name": movie_name,
            "Audience Score": movie_audience_score,
            "Rotten Tomato Score": movie_rottenTomato_score,
            "Budget": movie_budget,
            "Genre": movie_genre,
            "Studio": movie_studio,
            "Story": movie_story
        }
        
        
        movie_database[movie_name] = movie_info
        

sorted_movies = sorted(movie_database.items(), key=lambda x: x[0])
        
        
isActive = True
#isActive is for the main program runtime
while isActive == True:
    #have a ui for this in the future, but ask if user is an existing user
    print("I am reading keys:", readKeys())
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
        
        
        #user entry section:
        user_username_entry = str(input("Please enter your username"))
        user_password_entry = str(input("Please enter your password:"))
    elif existingUser == False:
        user_new_username_entry = str(input("Please enter your new username:"))
        user_new_password_entry = str(input("Please enter your new password:"))
    