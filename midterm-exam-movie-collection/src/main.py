"""
Midterm Practical Exam — Movie Collection Manager
Student: Ignacio, Justine Paul T.
"""

movies = []
movie_list = []
user_choice = 0


def display_menu():
    # print the menu
    # return the user's choice
    global user_choice
    print("=== Movie Collection Manager ===\n1. Add a movie\n2. View all movies\n3. Count watched vs unwatched\n4. Find a movie\n5. Exit")
    user_choice = int(input("Choose an option: "))
    match user_choice:
        case 1:
            add_movie(movie_list)

        case 2:
            view_movies(movie_list)

        case 3:
            count_watched_unwatched(movie_list)

        case 4:
            find_movie(movie_list)

        case 5:
            print("See you next time!")
    return user_choice


def add_movie(movie_list):
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    pending_movie = []
    print("Add a new movie\nExample: Inception - Christopher Nolan - Watched")

    new_movie_title = input("Enter movie title: ")
    pending_movie.append(new_movie_title)

    new_movie_director = input("Enter director: ")
    pending_movie.append(new_movie_director)

    new_movie_status = input("Enter status: ")
    pending_movie.append(new_movie_status)

    new_movie = "-".join(pending_movie)
    movie_list.append(new_movie)
    print(f"Successfully added {new_movie}")

    return display_menu()
    

def view_movies(movie_list):
    # loop through and print every movie
    # handle empty list
    print("=== Movie list ===")
    if len(movie_list) != 0:
        for m in enumerate(movie_list):
            print(f" {m}")
    else:
        print("Movie list is empty! Please add movies")
    return display_menu()
    


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    print("=== Movie watched count ===")
    if len(movie_list) != 0:
        pending_watch_count = [x.split("-") for x in movie_list]
        watched_count = pending_watch_count.count("watched")
        unwatched_count = pending_watch_count.count("unwatched")
        print(f"Number of watched movies: {watched_count}\nNumber of unwatched movies: {unwatched_count}")
    else:
        print("Movie list is empty! Please add movies")
    return display_menu()


def find_movie(movie_list):
    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    print("=== Find a movie ===")
    query_movie = input("Search for a movie: ").strip
    pending_find = [s.lower(query_movie) for s in movie_list]


def main():
    # create the main menu loop
    # call the appropriate function based on the user's choice
    while user_choice != 5:
        display_menu()



main()
