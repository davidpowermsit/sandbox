import json
import random
import statistics
from datetime import datetime

import matplotlib.pyplot as plt
from rapidfuzz.distance import Levenshtein

from sandbox.scrapbook.movie_Project import movie_storage

PADDING = 22
WIDTH = 47
FUZZYNESS = 2
MIN_RATING = 0
MAX_RATING = 10
MIN_YEAR = 1888  # first surviving film


def main() -> None:
    """Run the menu loop until the user chooses Exit."""
    try:
        run_menu()
    except (KeyboardInterrupt, EOFError):
        print()
    print(f"{' Bye! ':~^{WIDTH}}")


def run_menu() -> None:
    """Show the menu and run the chosen action until the user chooses Exit."""
    while True:
        try:
            movies = movie_storage.get_movies()
        except (json.JSONDecodeError, TypeError, OSError):
            print("Could not read the movie database. Please check data.json.")
            return

        choice = menu()

        try:
            match choice:
                case 0:
                    return
                case 1:
                    list_movies(movies)
                case 2:
                    add_movie(movies)
                case 3:
                    delete_movie(movies)
                case 4:
                    update_movie(movies)
                case 5:
                    stats(movies)
                case 6:
                    random_movie(movies)
                case 7:
                    search_movie(movies)
                case 8:
                    list_movies(movies, True)
                case 9:
                    create_histogram(movies)
        except OSError:
            print("Could not save your changes to the movie database.")


def prompt_text(prompt: str) -> str:
    """Ask until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def prompt_int(prompt: str, low: int, high: int) -> int:
    """Ask until the user enters a whole number between low and high."""
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("Please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")


def prompt_float(prompt: str, low: float, high: float) -> float:
    """Ask until the user enters a number between low and high."""
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Please enter a number.")
            continue
        if low <= value <= high:
            return value
        print(f"Please enter a number between {low} and {high}.")


def menu() -> int:
    """Display the menu and return the user's numeric choice."""
    print(f"{' My Movies Database ':~^{WIDTH + PADDING}}")

    print("Menu:")
    options = [
        "Exit",
        "List movies",
        "Add movie",
        "Delete movie",
        "Update movie",
        "Stats",
        "Random movie",
        "Search movie",
        "Movies sorted by rating",
        "Create Rating Histogram",
    ]

    for index, item in enumerate(options, 0):
        print(f"{index}. {item}")

    return prompt_int(f"Enter choice (0-{len(options) - 1}): ", 0, len(options) - 1)


def list_movies(movie_list: list[movie_storage.Movie], ranked: bool = False) -> None:
    """Print a table of the given movies with a total count."""
    if ranked:
        movie_list = sort_movies_by_rating(movie_list)

    print(f"\n{len(movie_list)} movies in total.\n")
    print(f"{'Title':<{WIDTH}}{'Rating':<6} {'Year'}")

    for m in movie_list:
        print(f"{m.title:<{WIDTH}}{m.rating:<6} {m.year}")


def add_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a title and rating, then add the movie if it is new."""
    print("\nEnter the Title, Rating and Year for a movie you would like to add.")
    title = prompt_text("Title: ")

    if movie_exists(movie_list, title):
        print(f"Movie {title!r} already exists.")
        return

    rating = prompt_float(f"Rating ({MIN_RATING}-{MAX_RATING}): ", MIN_RATING, MAX_RATING)
    year = prompt_int("Year: ", MIN_YEAR, datetime.now().year)

    movie_storage.add_movie(title, year, rating)
    print(f"Movie {title!r} - {rating!r} has been added.")


def delete_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a title and delete that movie if it exists."""
    title = prompt_text("\nWhich movie would you like to delete? ")

    movie = next((m for m in movie_list if m.title.lower() == title.lower()), None)
    if movie is not None:
        movie_storage.delete_movie(movie.title)
        print(f"Movie {title!r} has been deleted")
    else:
        print(f"No movie titled {title!r}")


def update_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a title and new rating, then update the movie if it exists."""
    title = prompt_text("Title: ")

    movie = next((m for m in movie_list if m.title.lower() == title.lower()), None)
    if movie is None:
        print(f"Could not find a movie called {title!r}")
        return

    rating = prompt_float(f"Rating ({MIN_RATING}-{MAX_RATING}): ", MIN_RATING, MAX_RATING)
    movie_storage.update_movie(movie.title, rating)
    print(f"Movie {movie.title!r} has been updated")


def stats(movie_list: list[movie_storage.Movie]) -> None:
    """Print average and median ratings plus the best and worst movies."""
    if not movie_list:
        print("\nNo movies in the database yet.")
        return

    average_rating = sum([m.rating for m in movie_list]) / len(movie_list)
    median_rating = statistics.median([m.rating for m in movie_list])

    ranked = sort_movies_by_rating(movie_list)
    top_rating = max([m.rating for m in ranked])
    top_movies = [movie for movie in ranked if movie.rating == top_rating]

    bottom_rating = min([m.rating for m in ranked])
    bottom_movies = [movie for movie in ranked if movie.rating == bottom_rating]

    print(f"{' Movie Stats ':~^{WIDTH + PADDING}}")

    print(f"Average Movie Rating: {average_rating:.2f}")
    print(f"Median Movie Rating: {median_rating:.2f}")

    print(f"{' Best Movie(s) ':-^{WIDTH + PADDING}}")
    if top_movies:
        print(f"{'Title':<{WIDTH}}{'Rating':<6} {'Year'}")
        for m in top_movies:
            print(f"{m.title:<{WIDTH}}{m.rating:<6} {m.year}")
    else:
        print(f"{' None ':-^{WIDTH + PADDING}}")

    print(f"{' Worst Movie(s) ':-^{WIDTH + PADDING}}")
    if bottom_movies:
        print(f"{'Title':<{WIDTH}}{'Rating':<6} {'Year'}")
        for m in bottom_movies:
            print(f"{m.title:<{WIDTH}}{m.rating:<6} {m.year}")
    else:
        print(f"{' None ':-^{WIDTH + PADDING}}")


def random_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Print a randomly chosen movie and its rating."""
    if not movie_list:
        print("\nNo movies in the database yet.")
        return

    m = random.choice(movie_list)  # noqa: S311
    print()
    print(f"{'Title':<{WIDTH}}{'Rating':<6} {'Year'}")
    print(f"{m.title:<{WIDTH}}{m.rating:<6} {m.year}")
    print()


def search_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a term and print movies whose titles contain it."""
    search = prompt_text("Enter a search term: ").lower()
    results = [m for m in movie_list if search in m.title.lower()]

    print(f"\nFound {len(results)!r} movies.")
    if len(results) == 0:
        print("The movie you wanted cound not be found. Please consider the following;\n")

    print(f"{'Title':<{WIDTH}}{'Rating':<6} {'Year'}")
    if results:
        for m in results:
            print(f"{m.title:<{WIDTH}}{m.rating:<6} {m.year}")
    else:
        fuzzy_results = [m for m in movie_list if Levenshtein.distance(m.title.lower(), search) <= FUZZYNESS]
        if fuzzy_results:
            for m in fuzzy_results:
                print(f"{m.title:<{WIDTH}}{m.rating:<6} {m.year}")
        else:
            print(f"{'Nothing was found. Sorry.':<{WIDTH}}\n")


def create_histogram(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a file name and save a histogram of the movie ratings to it."""
    filename = prompt_text("\nWhere would you like to save the histogram to? ")
    ratings = [m.rating for m in movie_list]
    plt.hist(ratings, bins=range(11), edgecolor="black")
    plt.title("Movie Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Number of movies")

    try:
        plt.savefig(filename)
        print(f"Histogram has been saved to {filename!r}")
    except (OSError, ValueError):
        print(f"Could not save the histogram to {filename!r}")
    finally:
        plt.close()


def movie_exists(movie_list: list[movie_storage.Movie], title: str) -> bool:
    """Using a generator with any, will return True as soon as a film is found"""
    return any(m.title.lower() == title.lower() for m in movie_list)


def sort_movies_by_rating(movie_list: list[movie_storage.Movie]) -> list[movie_storage.Movie]:
    """Return the movies sorted by rating, highest first."""
    return sorted(movie_list, key=lambda m: m.rating, reverse=True)


if __name__ == "__main__":
    main()
