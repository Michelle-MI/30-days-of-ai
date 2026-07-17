# Function 1

def add_student():
  name = input("What is your name: ")
  age = int(input("How old are you: "))
  university = input("What university do you attend: ")
  course = input("What course are you enrolled in: ")

  students = {
    "Name": name,
    "Age": age,
    "University": university,
    "Course": course
  }
  return students

students = add_student()
print(students)