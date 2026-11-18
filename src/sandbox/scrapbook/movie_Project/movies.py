import random
import statistics

import matplotlib.pyplot as plt
from rapidfuzz.distance import Levenshtein

from sandbox.scrapbook.movie_Project.movie_db import Movie, movies

small_padding = 2
large_padding = 22
width = max(len(m.title) for m in movies) + small_padding
FUZZYNESS = 2


def main() -> None:
    """Run the menu loop until the user chooses Exit."""
    while True:
        choice = menu()

        match choice:
            case 0:
                print(f"{' Bye! ':~^{width}}")
                break
            case 1:
                list_movies(movies)
            case 2:
                add_movie()
            case 3:
                delete_movie()
            case 4:
                update_movie()
            case 5:
                stats()
            case 6:
                random_movie()
            case 7:
                search_movie()
            case 8:
                list_movies(movies, True)
            case 9:
                create_histogram()


def menu() -> int:
    """Display the menu and return the user's numeric choice."""
    print(f"{' My Movies Database ':~^{width + large_padding}}")

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


def list_movies(movies: list[Movie], ranked: bool = False) -> None:
    """Print a table of the given movies with a total count."""
    if ranked:
        movies = sort_movies_by_rating(movies)

    print(f"\n{len(movies)} movies in total.\n")
    print(f"{'Title':<{width}}{'Rating':<6} {'Year'}")

    for m in movies:
        print(f"{m.title:<{width}}{m.rating:<6} {m.year}")


def add_movie() -> None:
    """Prompt for a title and rating, then add the movie if it is new."""
    print("\nEnter the Title and Rating for a movie you would like to add.")
    title = input("Title: ").strip()
    rating = float(input("Rating (0-10): "))
    year = int(input("Year: "))

    if movie_exists(movies, title):
        print(f"Movie {title!r} already exists.")
        return

    movies.append(Movie(title=title, rating=rating, year=year))
    print(f"Movie {title!r} - {rating!r} has been added.")


def delete_movie() -> None:
    """Prompt for a title and delete that movie if it exists."""
    title = input("\nWhich movie would you like to delete? ").strip()

    movie_del = next((m for m in movies if m.title.lower() == title.lower()), None)
    if movie_del is not None:
        movies.remove(movie_del)
        print(f"Movie {title!r} has been deleted")
    else:
        print(f"No movie titled {title!r}")


def update_movie() -> None:
    """Prompt for a title and new rating, then update the movie if it exists."""
    title = input("Title: ").strip()
    rating = float(input("Rating (0-10): "))
    year = int(input("Year: "))

    movie = next((m for m in movies if m.title.lower() == title.lower()), None)

    if movie is not None:
        movie.title = title
        movie.rating = rating
        movie.year = year
        print(f"Movie {title!r} has been updated")
    else:
        print(f"Could not find a movie called {title!r}")


def stats() -> None:
    """Print average and median ratings plus the best and worst movies."""
    average_rating = sum([m.rating for m in movies]) / len(movies)
    median_rating = statistics.median([m.rating for m in movies])

    ranked = sort_movies_by_rating(movies)
    top_rating = max([m.rating for m in ranked])
    top_movies = [movie for movie in ranked if movie.rating == top_rating]

    bottom_rating = min([m.rating for m in ranked])
    bottom_movies = [movie for movie in ranked if movie.rating == bottom_rating]

    print(f"{' Movie Stats ':~^{width + large_padding}}")

    print(f"Average Movie Rating: {average_rating:.2f}")
    print(f"Median Movie Rating: {median_rating:.2f}")

    print(f"{' Best Movie(s) ':-^{width + large_padding}}")
    if top_movies:
        print(f"{'Title':<{width}}{'Rating':<6} {'Year'}")
        for m in top_movies:
            print(f"{m.title:<{width}}{m.rating:<6} {m.year}")
    else:
        print(f"{' None ':-^{width + large_padding}}")

    print(f"{' Worst Movie(s) ':-^{width + large_padding}}")
    if bottom_movies:
        print(f"{m.title:<{width}}{m.rating:<6} {m.year}")

        for m in bottom_movies:
            print(f"{m.title:<{width}}{m.rating:<6} {m.year}")
    else:
        print(f"{' None ':-^{width + large_padding}}")


def random_movie() -> None:
    """Print a randomly chosen movie and its rating."""
    m = random.choice(movies)  # noqa: S311
    print()
    print(f"{'Title':<{width}}{'Rating':<6} {'Year'}")
    print(f"{m.title:<{width}}{m.rating:<6} {m.year}")
    print()


def search_movie() -> None:
    """Prompt for a term and print movies whose titles contain it."""
    search = input("Enter a search term: ").strip().lower()
    results = [m for m in movies if search in m.title.lower()]

    print(f"\nFound {len(results)!r} movies.")
    if len(results) == 0:
        print("The movie you wanted cound not be found. Please consider the following;\n")

    print(f"{'Title':<{width}}{'Rating':<6} {'Year'}")
    if results:
        for m in results:
            print(f"{m.title:<{width}}{m.rating:<6} {m.year}")
    else:
        fuzzy_results = [m for m in movies if Levenshtein.distance(m.title.lower(), search) <= FUZZYNESS]
        if fuzzy_results:
            for m in fuzzy_results:
                print(f"{m.title:<{width}}{m.rating:<6} {m.year}")
        else:
            print(f"{'Nothing was found. Sorry.':<{width}}\n")


def create_histogram() -> None:
    """Prompt for a file name and save a histogram of the movie ratings to it."""
    filename = input("\nWhere would you like to save the histogram to? ").strip()
    ratings = [m.rating for m in movies]
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


def movie_exists(movies: list[Movie], title: str) -> bool:
    """Using a generator with any, will return True as soon as a film is found"""
    return any(m.title.lower() == title.lower() for m in movies)


def sort_movies_by_rating(movies: list[Movie]) -> list[Movie]:
    return sorted(movies, key=lambda m: m.rating, reverse=True)


if __name__ == "__main__":
    main()
