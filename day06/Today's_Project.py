# Today's Project - Student Profile

name = input("Enter your name: ")
age = int(input("How old are you: "))
university = input("Which university do you attend: ")
course = input("What course are you enrolled in: ")
favorite_language = input("What is your favorite programming language: ")

student_profile = {
  "Name": name,
  "Age": age,
  "University": university,
  "Course": course,
  "Favorite Language": favorite_language
}
print(student_profile)


# Stretch Challenge

students = {
  "Michelle": {
    "Age": 23,
    "Course": "Computer Science",
    "Favorite Language": "Python"
  },
  "Brian": {
    "Age": 22,
    "Course": "Computer Science",
    "Favorite Language": "Kotlin"
  },
  "Grace": {
    "Age": 24,
    "Course": "Software Engineering",
    "Favorite Language": "JavaScript"
  }
}
print(students)