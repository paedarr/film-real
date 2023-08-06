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
        
        movie_info = {
            "name": movie_name,
            "rating": movie_rating,
            "budget": movie_budget,
        }
        
        movie_database[movie_name] = movie_info
        
        
sorted_movies = sorted(movie_database.items(), key=lambda x: x[0])
        

