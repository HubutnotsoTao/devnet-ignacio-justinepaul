"""
Midterm Practical Exam — Movie Collection Manager
Student: Ignacio, Justine Paul T.
"""

movies = []


def display_menu():
    # print the menu
    # return the user's choice
    print("=== Movie Collection Manager ===\n1. Add a movie\n2. View all movies\n3. Count watched vs unwatched\n4. Find a movie\n5. Exit")
    user_choice = int(input("Choose an option: "))

    while True:
        match user_choice:
            case 1:
                add_movie()

            case 2:
                view_movies()

            case 3:
                count_watched_unwatched()

            case 4:
                find_movie()

            case 5:
                print("See you next time!")
                return False


def add_movie(movie_list):
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    print("Add a movie")
    


def view_movies(movie_list):
    # loop through and print every movie
    # handle empty list
    print("Movie list")
    


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    print("Movie watchlist")


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    print("Find a movie")


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    display_menu()



main()
