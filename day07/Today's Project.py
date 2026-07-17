# Today's Project - Student Management System

students = []

def add_student(): 
  name = input("What is your name: ")
  age = int(input("How old are you: "))
  course = input("What course are you enrolled in: ")

  student = {
    "name": name,
    "age": age,
    "course": course
  }
  return student

def display_students(students):
  for student in students:
    print("\n----Students List---")
    print("Name: ", student["name"])
    print("Age: ", student["age"])
    print("Course: ", student["course"])
    print("-------------------------")

number = int(input("How many students would you like to enter: "))

for _ in range(number):
  student = add_student()
  students.append(student)

display_students(students)

# Stretch Challenge

search = input("Search for a student by name: ")

found = False

for student in students:
  if student["name"].lower() == search.lower():
    print("\nStudent Found")
    print("Name: ", student["name"])
    print("Age: ", student["age"])
    print("Course: ", student["course"])
    found = True
    break

if not found:
    print("Student not found.")

    