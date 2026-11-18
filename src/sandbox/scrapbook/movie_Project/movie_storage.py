import json
from dataclasses import dataclass
from pathlib import Path
from typing import TypedDict, cast


# Learned about dataclass:
# - It gives m.rating instead of item[1]["rating"]
@dataclass
class Movie:
    title: str
    rating: float
    year: int


# Learned about typedDict so I can better use type hinting
# - it enables unpacking like this Movie(title=t, **info)
class MovieInfo(TypedDict):
    rating: float
    year: int


MOVIE_FILE = Path(__file__).parent / "data.json"


def get_movies() -> list[Movie]:
    """
    Returns a list of Movies that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.
    """

    with MOVIE_FILE.open() as f:
        movies = cast("dict[str, MovieInfo]", json.load(f))

    return [Movie(title=t, **info) for t, info in movies.items()]


def save_movies(movies: list[Movie]) -> None:
    """
    Gets all your movies as an argument and saves them to the JSON file.
    """
    data = {m.title: MovieInfo(rating=m.rating, year=m.year) for m in movies}

    with MOVIE_FILE.open("w") as f:
        json.dump(data, f, indent=2)


def add_movie(title: str, year: int, rating: float) -> None:
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    movies.append(Movie(title=title, rating=rating, year=year))
    save_movies(movies)


def delete_movie(title: str) -> None:
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = [m for m in get_movies() if m.title.lower() != title.lower()]
    save_movies(movies)


def update_movie(title: str, rating: float) -> None:
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = get_movies()
    for m in movies:
        if m.title.lower() == title.lower():
            m.rating = rating
    save_movies(movies)
