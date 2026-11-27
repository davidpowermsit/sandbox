import json
import statistics
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "json"

print("Chapter Assessment - JSON\n")
# --------------------------------------------------------------------------
print("Question 1 - \n")

with open(DATA_DIR / "grades.json") as grades_file:
    students = json.load(grades_file)  # list[dict]

for student in students:
    grades = student["grades"]

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

with open(DATA_DIR / "grades_analysis.json", "w") as grade_obj:
    json.dump(student_analytics, grade_obj)
# --------------------------------------------------------------------------
print("Question 3 - \n")
