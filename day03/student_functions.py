# Function 1
# def greet_student(name):

# Print a welcome message.

from pyclbr import Function


def greet_student(name):
  print("Welcome,", name, "to AI Engieering Program")

# Function 2
# def check_voting(age):

# Return:

# "Eligible to vote"
# "Not eligible to vote"

def check_voting(age):
  if age >= 18:
    print("Eligible to vote")
  else:
    print("Not eligible to vote")


# Function 3
# def study_feedback(hours):

#Return:

#Excellent consistency!
# Great job! Keep improving.
# Small daily improvements lead to big results.

def study_feedback(hours):
  if hours >= 5:
    print("Excellent consistency!")
  elif hours >= 3 and hours <= 4:
    print("Great job! Keep improving.")
  else:
    print("Small daily improvements lead to big results.")

# Then ask the user for:

# Name
# Age
# Study hours

# Call the functions and display the results.

name = input("What is your name: ")
age = int(input("How old are you: "))
hours = int(input("How many hours do you study per day: "))

greet_student(name)
check_voting(age)
study_feedback(hours)

# Stretch challenge
# Create:

# def calculate_average(math, science, english):

# Return the average.

# Then determine:

# Average ≥ 70 → Excellent
# Average ≥ 50 → Good
# Otherwise → Keep practicing

def calculate_average(math, science, english):
 total = math + science + english
 average = total / 3

 print(average)

 if average >= 70:
    print("Excellent")
 elif average >= 50:
    print("Good")
 else:
    print("Keep practicing")

 return average

math =int(input("what did you score in your math exam: "))
science =int(input("what did you score in your science exam: "))
english =int(input("what did you score in your english exam: "))

calculate_average(math, science, english)



