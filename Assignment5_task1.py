import re
student_marks = {
    "Alice": 85,
    "Bob": 76,
    "Charlie": 92,
    "David": 65
}
name = input("Enter the student's name: ")
pattern = r"\b" + re.escape(name) + r"\b"
data = " ".join(student_marks.keys())
match_obj = re.search(pattern, data)
if match_obj:
    print(name, "marks:", student_marks[name])
else:
    print("Student not found.")