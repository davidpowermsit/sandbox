from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "txt"

timesheet_path = DATA_DIR / "timesheet.rtf"


months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]

countries = [
    {"name": "Spain", "capital_city": "Madrid", "currency": "EUR"},
    {"name": "United States", "capital_city": "Washington", "currency": "USD"},
    {"name": "Canada", "capital_city": "Ottawa", "currency": "CAD"},
]

print("Chapter Assessment - Writing Files\n")
# --------------------------------------------------------------------------
print("Question 1 - Search and Replace\n")


def search_and_replace() -> None:
    filename = input("Filename: ")
    old_word = input("Word to replace: ")
    new_word = input("Replacement word: ")

    with open(filename) as source:
        text = source.read()

    with open(filename + ".new", "w") as target:
        target.write(text.replace(old_word, new_word))


# --------------------------------------------------------------------------
print("Question 2 - Timesheet files\n")


def create_timesheet_files() -> None:
    # Load the timesheet file
    with open(timesheet_path) as fileobj:
        timesheet = fileobj.read().strip()

    for month in months:
        with open(DATA_DIR / f"timesheet_{month}23.rtf", "w") as month_fileobj:
            month_fileobj.write(timesheet)


# --------------------------------------------------------------------------
print("Question 3 - Country files\n")


def create_country_info() -> None:
    for entry in countries:
        country, city, currency = entry.values()
        with open(DATA_DIR / f"{country}.txt", "w") as fileobj:
            fileobj.write(f"City: {city}\nCurrency: {currency}")


create_country_info()
