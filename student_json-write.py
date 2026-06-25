import json

student = {
    "name": "Anu",
    "course": "Django",
    "age": 22
}

with open("new_student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Data written successfully.")