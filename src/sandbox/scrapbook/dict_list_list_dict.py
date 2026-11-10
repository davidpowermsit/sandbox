# mypy: disable-error-code="index"
import statistics

# List of dictionaries: Each dictionary represents additional information about a student.
student_info = [
    {"name": "Alice", "age": 18, "gender": "female"},
    {"name": "Bob", "age": 17, "gender": "male"},
    {"name": "Charlie", "age": 18, "gender": "male"},
]

# Dictionary of dictionaries: Each inner dictionary represents additional information about a student.
student_details = {
    "Alice": {"city": "New York", "grade_level": "Senior"},
    "Bob": {"city": "Los Angeles", "grade_level": "Junior"},
    "Charlie": {"city": "Chicago", "grade_level": "Senior"},
}


# List of lists: Each inner list represents the grades of a student.
student_grades = [[85, 90, 88], [75, 80, 82], [92, 95, 89]]

print(f"\n{'Students':~^40}")
for info, grade in zip(student_info, student_grades, strict=True):
    details = student_details[info["name"]]
    print(f"Student: {info['name']}")
    print(f"Age: {info['age']}")
    print(f"Average Grade: {round(statistics.mean(grade), 2)}")
    print(f"Grade Level: {details['grade_level']}")
    print()
