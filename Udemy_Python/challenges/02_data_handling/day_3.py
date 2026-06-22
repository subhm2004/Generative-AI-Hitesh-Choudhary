# ============================================================
# FILE: day_3.py
# TOPIC: JSON read/write, list of dicts, match-case
# FOLDER: challenges/02_data_handling
# CHALLENGE DAY: Day 3
# ============================================================
# Yeh challenge sikhata hai:
# - JSON = JavaScript Object Notation (structured data format)
# - json.load() = file se Python object (list/dict) mein convert
# - json.dump() = Python object ko JSON file mein save
# - List of dictionaries = movies database jaisa structure
# - any() = kya koi movie title match karta hai? (duplicate check)
# ============================================================

"""
 Challenge:  Personal Movie Tracker with JSON

Create a Python CLI tool that lets users maintain their own personal movie database, like a mini IMDb.

Your program should:
1. Store all movie data in a `movies.json` file.
2. Each movie should have:
   - Title
   - Genre
   - Rating (out of 10)
3. Allow the user to:
   - Add a movie
   - View all movies
   - Search movies by title or genre
   - Exit the app

Bonus:
- Prevent duplicate titles from being added
- Format output in a clean table
- Use JSON for reading/writing structured data
"""

import os
import json

FILENAME = "movies.json"

# JSON file se movies load karo (list of dicts return hoga)
def load_movies():
    if not os.path.exists(FILENAME):
        return []  # file nahi hai to khali list
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)  # JSON text -> Python list/dict
    
def save_movies(movies):
    with open(FILENAME, "w", encoding="utf-8") as f:
        # indent=2 = pretty formatting (readable JSON file)
        json.dump(movies, f, indent=2)


def add_movies(movies):
    title = input("Enter the movie name: ").strip().lower()

    # any() = kya KOI bhi movie ka title match karta hai?
    if any(movie["title"].lower() == title for movie in movies):
        print("Movie already exists")
        return
    genre = input("Genre: ").strip().lower()
    try:
        rating = float(input("Enter rating(0-10): "))
        # Rating 0 se 10 ke beech honi chahiye
        if not (0 <= rating <= 10):
            raise ValueError
    except ValueError:
        print("Please enter valid number")
        return
    
    # Naya movie dict banake list mein append karo
    movies.append({"title": title, "genre": genre, "rating": rating})
    save_movies(movies)
    print("Movie added ✅")
    
    
def search_movies(movies):
    term = input("Enter the title or genre: ").strip().lower()

    # List comprehension se matching movies filter karo
    results = [
        movie for movie in movies 
        if term in movie['title'].lower() or term in movie['genre'].lower()
     
    ]
    if not results:
        print("No matching result")
        return
    print(f" Found {len(results)} result(s)")

    for movie in results:
        print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")


def view_movies(movies):
    if not movies:
        print("NO movies in DB")
        return
    print("-"*30)
    for movie in movies:
        print(f"{movie["title"]} -- {movie["genre"]} -- {movie["rating"]}")
    print("-"*30)



def run_movie_db():
    movies = load_movies()  # start mein file se data load

    while True:
        print("\n🍿 MyMovieDB")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Exit")
    
        choice = input("Choose an option (1-4): ").strip()
        match choice:
            case "1": add_movies(movies)
            case "2": view_movies(movies)
            case "3": search_movies(movies)
            case "4": break
            case _: print("Enter valid choice") 


if __name__ == "__main__":
    run_movie_db()
