from sandbox.scrapbook.imdb250.database import dennys_movies

DB = dennys_movies

# ✏️ Your Tasks
# Write a function get_title_by_rank(rank)
# - It should receive a rank number and return the movie title.
# Write a function get_rank_by_title(title)
# - It should receive a movie title and return its rank.


def main() -> None:
    choice_rank = 2
    choice_film = "The Godfather"

    name = get_title_by_rank(choice_rank)
    rank = get_rank_by_title(choice_film)

    print(f"The film for rank {choice_rank!r} is {name!r}")
    print(f"The rank for film {choice_film!r} is {rank!r}")


def get_title_by_rank(rank: int) -> str:
    return DB[rank - 1]["name"]


def get_rank_by_title(title: str) -> int | None:
    for movie in DB:
        if movie["name"] == title:
            return movie["imdb_rank"]
    return None


if __name__ == "__main__":
    main()
