import random
import statistics

from sandbox.scrapbook.movie_db import bottom_5, movies, ranked_movies, top_5

padding = 2
width = max(len(title) for title in movies) + padding


def main() -> None:
    """Run the menu loop until the user chooses Exit."""
    while True:
        choice = menu()

        match choice:
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
                list_movies(ranked_movies)
            case 9:
                print(f"{' Program Ended ':~^{width}}")
                break


def menu() -> int:
    """Display the menu and return the user's numeric choice."""
    print(f"{' My Movies Database ':~^{width}}")

    print("Menu:")
    options = [
        "List movies",
        "Add movie",
        "Delete movie",
        "Update movie",
        "Stats",
        "Random movie",
        "Search movie",
        "Movies sorted by rating",
        "Exit",
    ]

    for index, item in enumerate(options, 1):
        print(f"{index}. {item}")

    choice = (int)(input(f"Enter choice (1-{len(options)}): ").strip())
    return choice


def list_movies(movies: dict[str, float]) -> None:
    """Print a table of the given movies with a total count."""
    print(f"\n{len(movies)} movies in total.\n")
    print(f"{'Title':<{width}}{'Rating'}")

    for title, rating in movies.items():
        print(f"{title:<{width}}{rating}")


def add_movie() -> None:
    """Prompt for a title and rating, then add the movie if it is new."""
    print("\nEnter the Title and Rating for a movie you would like to add.")
    title = input("Title: ").strip()
    rating = float(input("Rating (0-10): "))

    if title in movies:
        print(f"Movie {title!r} already exists.")
        return

    movies[title] = rating
    print(f"Movie {title!r} - {rating!r} has been added.")


def delete_movie() -> None:
    """Prompt for a title and delete that movie if it exists."""
    title = input("\nWhich movie would you like to delete? ").strip()
    try:
        del movies[title]
        print(f"Movie {title!r} has been deleted")
    except KeyError:
        print(f"Could not find a movie called {title!r}")


def update_movie() -> None:
    """Prompt for a title and new rating, then update the movie if it exists."""
    title = input("Title: ").strip()
    rating = float(input("Rating (0-10): "))

    if title not in movies:
        print(f"Could not find a movie called {title!r}")
        return

    movies[title] = rating
    print(f"Movie {title!r} has been updated")


def stats() -> None:
    """Print average and median ratings plus the best and worst movies."""
    average_rating = sum(movies.values()) / len(movies)
    median_rating = statistics.median(movies.values())

    print(f"{' Movie Stats ':~^{width}}")

    print(f"Average Movie Rating: {average_rating:.2f}")
    print(f"Median Movie Rating: {median_rating:.2f}")

    print(f"{' Best Movie(s) ':-^{width}}")
    if top_5:
        print(f"{'Title':<{width}}{'Rating'}")
        for title, rating in top_5.items():
            print(f"{title:<{width}}{rating}")
    else:
        print(f"{' None ':-^{width}}")

    print(f"{' Worst Movie(s) ':-^{width}}")
    if bottom_5:
        print(f"{'Title':<{width}}{'Rating'}")
        for title, rating in bottom_5.items():
            print(f"{title:<{width}}{rating}")
    else:
        print(f"{' None ':-^{width}}")


def random_movie() -> None:
    """Print a randomly chosen movie and its rating."""
    title, rating = random.choice(list(movies.items()))  # noqa: S311
    print()
    print(f"{'Title':<{width}}{'Rating'}")
    print(f"{title:<{width}}{rating}")
    print()


def search_movie() -> None:
    """Prompt for a term and print movies whose titles contain it."""
    search = input("Enter a search term: ").strip().lower()
    results = {title: rating for title, rating in movies.items() if search in title.lower()}

    print(f"\nFound {len(results)!r} movies.\n")
    print(f"{'Title':<{width}}{'Rating'}")
    if results:
        for title, rating in results.items():
            print(f"{title:<{width}}{rating}")
    else:
        print(f"{'Nothing Found':<{width}}")
    print()


if __name__ == "__main__":
    main()
