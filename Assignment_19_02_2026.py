
students = [
    {"name": "Alice", "math": 85, "science": 90, "english": 88},
    {"name": "Bob", "math": 78, "science": 82, "english": 80},
    {"name": "Charlie", "math": 92, "science": 88, "english": 95},
    {"name": "Diana", "math": 88, "science": 91, "english": 89},
    {"name": "Eve", "math": 75, "science": 79, "english": 81}
]


for student in students:
    avg = (student["math"] + student["science"] + student["english"]) / 3
    student["average"] = avg
    
    if avg >= 90:
        student["grade"] = "A"
    elif avg >= 80:
        student["grade"] = "B"
    elif avg >= 70:
        student["grade"] = "C"
    else:
        student["grade"] = "D"


topper = max(students, key=lambda x: x["average"])
print(f"Topper: {topper['name']} with average {topper['average']:.2f}")


class_avg = sum(s["average"] for s in students) / len(students)
print(f"Class Average: {class_avg:.2f}")


print("\nStudent Grades:")
for student in students:
    print(f"{student['name']}: {student['average']:.2f} - Grade {student['grade']}")