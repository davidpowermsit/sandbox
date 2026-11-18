from dataclasses import dataclass
from typing import TypedDict


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


movie_import: dict[str, MovieInfo] = {
    "The Shawshank Redemption": {"rating": 9.5, "year": 1994},
    "Pulp Fiction": {"rating": 8.8, "year": 1994},
    "The Room": {"rating": 3.6, "year": 2003},
    "The Godfather": {"rating": 9.2, "year": 1972},
    "The Godfather: Part II": {"rating": 9.0, "year": 1974},
    "The Dark Knight": {"rating": 9.0, "year": 2008},
    "12 Angry Men": {"rating": 8.9, "year": 1957},
    "Everything Everywhere All At Once": {"rating": 8.9, "year": 2022},
    "Forrest Gump": {"rating": 8.8, "year": 1994},
    "Star Wars: Episode V": {"rating": 8.7, "year": 1980},
    "Schindler's List": {"rating": 9.0, "year": 1993},
    "The Lord of the Rings: The Return of the King": {"rating": 9.0, "year": 2003},
    "The Good, the Bad and the Ugly": {"rating": 8.8, "year": 1966},
    "Fight Club": {"rating": 8.8, "year": 1999},
    "Inception": {"rating": 8.8, "year": 2010},
    "The Matrix": {"rating": 8.7, "year": 1999},
    "Goodfellas": {"rating": 8.7, "year": 1990},
    "One Flew Over the Cuckoo's Nest": {"rating": 8.7, "year": 1975},
    "Se7en": {"rating": 8.6, "year": 1995},
    "Interstellar": {"rating": 8.7, "year": 2014},
    "The Silence of the Lambs": {"rating": 8.6, "year": 1991},
    "Saving Private Ryan": {"rating": 8.6, "year": 1998},
    "City of God": {"rating": 8.6, "year": 2002},
    "Life Is Beautiful": {"rating": 8.6, "year": 1997},
    "The Green Mile": {"rating": 8.6, "year": 1999},
    "Terminator 2: Judgment Day": {"rating": 8.6, "year": 1991},
    "Back to the Future": {"rating": 8.5, "year": 1985},
    "Spirited Away": {"rating": 8.6, "year": 2001},
    "Parasite": {"rating": 8.5, "year": 2019},
    "Léon: The Professional": {"rating": 8.5, "year": 1994},
    "The Usual Suspects": {"rating": 8.5, "year": 1995},
    "The Pianist": {"rating": 8.5, "year": 2002},
    "Gladiator": {"rating": 8.5, "year": 2000},
    "The Departed": {"rating": 8.5, "year": 2006},
    "Whiplash": {"rating": 8.5, "year": 2014},
    "The Prestige": {"rating": 8.5, "year": 2006},
    "Casablanca": {"rating": 8.5, "year": 1942},
    "Alien": {"rating": 8.5, "year": 1979},
    "Psycho": {"rating": 8.5, "year": 1960},
    "Apocalypse Now": {"rating": 8.4, "year": 1979},
    "Memento": {"rating": 8.4, "year": 2000},
    "Raiders of the Lost Ark": {"rating": 8.4, "year": 1981},
    "Django Unchained": {"rating": 8.5, "year": 2012},
    "WALL·E": {"rating": 8.4, "year": 2008},
    "The Lion King": {"rating": 8.5, "year": 1994},
    "American History X": {"rating": 8.5, "year": 1998},
    "Joker": {"rating": 8.4, "year": 2019},
    "Coco": {"rating": 8.4, "year": 2017},
    "Oldboy": {"rating": 8.3, "year": 2003},
    "Toy Story": {"rating": 8.3, "year": 1995},
    "Braveheart": {"rating": 8.3, "year": 1995},
    "Amadeus": {"rating": 8.3, "year": 1984},
    "Good Will Hunting": {"rating": 8.3, "year": 1997},
    "Reservoir Dogs": {"rating": 8.3, "year": 1992},
    "Taxi Driver": {"rating": 8.2, "year": 1976},
    "Full Metal Jacket": {"rating": 8.3, "year": 1987},
    "A Clockwork Orange": {"rating": 8.3, "year": 1971},
    "The Shining": {"rating": 8.4, "year": 1980},
    "Blade Runner": {"rating": 8.1, "year": 1982},
    "Heat": {"rating": 8.3, "year": 1995},
    "Die Hard": {"rating": 8.2, "year": 1988},
    "Up": {"rating": 8.3, "year": 2009},
    "Inglourious Basterds": {"rating": 8.4, "year": 2009},
    "Monty Python and the Holy Grail": {"rating": 8.2, "year": 1975},
    "Scarface": {"rating": 8.3, "year": 1983},
    "Jaws": {"rating": 8.1, "year": 1975},
    "The Truman Show": {"rating": 8.2, "year": 1998},
    "Gran Torino": {"rating": 8.1, "year": 2008},
    "Mad Max: Fury Road": {"rating": 8.1, "year": 2015},
    "Her": {"rating": 8.0, "year": 2013},
    "Shaun of the Dead": {"rating": 7.9, "year": 2004},
    "Ghostbusters": {"rating": 7.8, "year": 1984},
    "Top Gun: Maverick": {"rating": 8.2, "year": 2022},
    "Dune": {"rating": 8.0, "year": 2021},
    "The Social Network": {"rating": 7.8, "year": 2010},
    "Logan": {"rating": 8.1, "year": 2017},
    "Gravity": {"rating": 7.7, "year": 2013},
    "Jurassic Park": {"rating": 8.2, "year": 1993},
    "Titanic": {"rating": 7.9, "year": 1997},
    "Avatar": {"rating": 7.9, "year": 2009},
    "The Avengers": {"rating": 8.0, "year": 2012},
    "Black Panther": {"rating": 7.3, "year": 2018},
    "Iron Man": {"rating": 7.9, "year": 2008},
    "Rocky": {"rating": 8.1, "year": 1976},
    "Ferris Bueller's Day Off": {"rating": 7.8, "year": 1986},
    "The Big Lebowski": {"rating": 8.1, "year": 1998},
    "Superbad": {"rating": 7.6, "year": 2007},
    "Anchorman": {"rating": 7.2, "year": 2004},
    "Step Brothers": {"rating": 6.9, "year": 2008},
    "The Hangover": {"rating": 7.7, "year": 2009},
    "Twilight": {"rating": 5.3, "year": 2008},
    "Batman & Robin": {"rating": 3.8, "year": 1997},
    "Catwoman": {"rating": 3.4, "year": 2004},
    "Battlefield Earth": {"rating": 2.5, "year": 2000},
    "Cats": {"rating": 2.8, "year": 2019},
    "Plan 9 from Outer Space": {"rating": 4.0, "year": 1957},
    "Gigli": {"rating": 2.5, "year": 2003},
    "Movie 43": {"rating": 4.3, "year": 2013},
    "Sharknado": {"rating": 3.3, "year": 2013},
    "Transformers: Revenge of the Fallen": {"rating": 6.0, "year": 2009},
}

movies = [Movie(title=t, **info) for t, info in movie_import.items()]
