# Function 1

def greet_student(name):
  print("Welcome,", name, "to AI Engieering Program")

# Function 2

def check_voting(age):
  if age >= 18:
    print("Eligible to vote")
  else:
    print("Not eligible to vote")


# Function 3

def study_feedback(hours):
  if hours >= 5:
    print("Excellent consistency!")
  elif hours >= 3 and hours <= 4:
    print("Great job! Keep improving.")
  else:
    print("Small daily improvements lead to big results.")


name = input("What is your name: ")
age = int(input("How old are you: "))
hours = int(input("How many hours do you study per day: "))

greet_student(name)
check_voting(age)
study_feedback(hours)


# Stretch challenge

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



