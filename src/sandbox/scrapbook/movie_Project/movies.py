import random
import statistics

import matplotlib.pyplot as plt
from rapidfuzz.distance import Levenshtein

from sandbox.scrapbook.movie_Project import movie_storage

PADDING = 22
WIDTH = 47
FUZZYNESS = 2


def main() -> None:
    """Run the menu loop until the user chooses Exit."""
    while True:
        movies = movie_storage.get_movies()
        choice = menu()

        match choice:
            case 0:
                print(f"{' Bye! ':~^{WIDTH}}")
                break
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

    choice = (int)(input(f"Enter choice (1-{len(options)}): ").strip())
    return choice


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
    print("\nEnter the Title and Rating for a movie you would like to add.")
    title = input("Title: ").strip()
    rating = float(input("Rating (0-10): "))
    year = int(input("Year: "))

    if movie_exists(movie_list, title):
        print(f"Movie {title!r} already exists.")
        return

    movie_storage.add_movie(title, year, rating)
    print(f"Movie {title!r} - {rating!r} has been added.")


def delete_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a title and delete that movie if it exists."""
    title = input("\nWhich movie would you like to delete? ").strip()

    movie = next((m for m in movie_list if m.title.lower() == title.lower()), None)
    if movie is not None:
        movie_storage.delete_movie(movie.title)
        print(f"Movie {title!r} has been deleted")
    else:
        print(f"No movie titled {title!r}")


def update_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a title and new rating, then update the movie if it exists."""
    title = input("Title: ").strip()
    rating = float(input("Rating (0-10): "))

    movie = next((m for m in movie_list if m.title.lower() == title.lower()), None)

    if movie is not None:
        movie_storage.update_movie(movie.title, rating)
        print(f"Movie {movie.title!r} has been updated")
    else:
        print(f"Could not find a movie called {title!r}")


def stats(movie_list: list[movie_storage.Movie]) -> None:
    """Print average and median ratings plus the best and worst movies."""
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
    m = random.choice(movie_list)  # noqa: S311
    print()
    print(f"{'Title':<{WIDTH}}{'Rating':<6} {'Year'}")
    print(f"{m.title:<{WIDTH}}{m.rating:<6} {m.year}")
    print()


def search_movie(movie_list: list[movie_storage.Movie]) -> None:
    """Prompt for a term and print movies whose titles contain it."""
    search = input("Enter a search term: ").strip().lower()
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
    filename = input("\nWhere would you like to save the histogram to? ").strip()
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
