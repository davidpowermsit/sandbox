from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "csv"

spain_medals_path = DATA_DIR / "spain-medals.csv"
grades_path = DATA_DIR / "grades.csv"


def writing_files_exercises() -> None:

    print("Print Gold Medals\n")

    with open(spain_medals_path) as spain_file:
        spin_data = spain_file.readlines()

    medal_count = 0
    for line in spin_data:
        if "Women's" in line and "Gold" in line:
            medal_count += 1

    print(f"Women's Gold Medal Count: {medal_count}")
    print()

    # ----------------------------------------------------------------------------

    print("Print Student Scores\n")

    with open(grades_path) as fileobj:
        lines = fileobj.readlines()

    for line in lines[1:]:
        _, score, _ = line.split(",")
        print(f"{score}")

    print()
    # ----------------------------------------------------------------------------

    print("Print Student Scores in scale (0-10)\n")

    with open(grades_path) as fileobj:
        lines = fileobj.readlines()
        for line in lines[1:]:
            _, score, _ = line.split(",")
            print(f"{int(score) / 10:.1f}")

    print()


# ----------------------------------------------------------------------------


def writing_files_exercise_4_bonus() -> None:
    with open(grades_path) as source:
        text = source.read().strip()

    lines = text.split()

    with open(DATA_DIR / "grades-full.csv", "w") as copy:
        copy.write(lines[0] + ",Assessment\n")
        for line in lines[1:]:
            name, score, grade = line.split(",")
            assessment = "Passed" if int(score) >= 90 else "Failed"
            copy.write(",".join([name, score, grade, assessment]) + "\n")


writing_files_exercise_4_bonus()
