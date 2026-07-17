# function 2

def display_students(students):
  print("\n----Student List----")

  for student in students:
    print("Name: ", student["Name"])
    print("Age: ", student["Age"])
    print("University: ", student["University"])
    print("Course: ", student["Course"])
    print("-------------------------------------")

