import datetime as dt

top_fruits = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]


def all_or_nothing(gamble: list[str]) -> list | None:
    if len(gamble) > 0:
        return gamble * 2
    return gamble


# Write a function, remove_ends, that accepts a list as input and returns a new list with the first and last elements removed.
# You can assume the given list contains at least two items.

# Example:
# >> remove_ends(["Jack", "Rose", "Cal"])
# ["Rose"]
# >> remove_ends([12, 50, 651, 64, 23])
# [50, 651, 64]


def remove_ends(process: list) -> list:
    if len(process) >= 2:
        return process[1:-1]
    return process


# set running to to get the code to run True

fruits = ["apple", "banana", "cherry", "banana"]

running = False
while running:
    choice = input("Type Add, Remove, List or Exit: ").strip().lower()

    if choice == "add":
        fruit = input("Which fruit do you want to add? ").strip()
        fruits.append(fruit)
    elif choice == "remove":
        if fruits:
            fruits.pop()
        else:
            print("The list is already empty.")
    elif choice == "exit":
        running = False
    elif choice == "list":
        print(f"\n{fruits}\n")
    else:
        print("Oops - Please type Add, List, Remove or Exit.")


# Code Challenge · Grade Range


def average(num_list: list[int]) -> float:
    return round(sum(num_list) / len(num_list), 2)


def grade_range(grades: list[int]) -> int:
    return max(grades) - min(grades)


dt.datetime.strptime("31/01/22 23:59:59.999999", "%d/%m/%y %H:%M:%S.%f")


def parse_timestamp(text: str) -> dt.datetime:
    return dt.datetime.strptime(text, "%d/%m/%y %H:%M:%S.%f")
