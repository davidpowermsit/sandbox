import json
import statistics
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "json"

print("Chapter Assessment - JSON\n")
# --------------------------------------------------------------------------
print("Question 1 - \n")

try:
    with open(DATA_DIR / "grades.json") as grades_file:
        students = json.load(grades_file)  # list[dict]
except FileNotFoundError:
    print("grades.json not found")
    students = []
except json.JSONDecodeError as err:
    print(f"grades.json is not valid JSON: {err}")
    students = []

for student in students:
    grades = student["grades"]

    if not grades:
        print(f"{student['name']} has no grades\n")
        continue

    average = statistics.mean(grades)
    low = min(grades)
    high = max(grades)

    print(student["name"])
    print(f"Average: {average} - Lowest:{low} Highest: {high}.\n")

# --------------------------------------------------------------------------
print("Question 2 - \n")

student_analytics: list[dict] = []
for student in students:
    student_analytics.append({
        "name": student["name"],
        "average": average,
        "lowest": low,
        "highest": high,
    })

try:
    with open(DATA_DIR / "grades_analysis.json", "w") as grade_obj:
        json.dump(student_analytics, grade_obj)
except PermissionError:
    print("No permission to write grades_analysis.json")

# --------------------------------------------------------------------------
print("Question 3 - \n")
