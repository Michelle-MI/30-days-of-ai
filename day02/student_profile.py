# Today's Project
# Create a program called:

# student_profile.py

# Requirements:

# Ask the user for:
# Name
# Age
# University
# Course
# Favorite programming language
# Print a beautiful summary.
# If age is 18 or older, print:
#You are eligible to vote.

#Otherwise print:

#You are not yet eligible to vote.
#Finally print:
#Thank you for using the Student Profile Generator!

name = input("What is your name? ")
age = int(input("How old are you? "))

if age >= 18:
  print("You are elgible to vote.")
else:
  print("You are not elgible to vote.")


university = input("Which university do you attend? ")
course = input("What course are you studying? ")
programming_language = input("What is your favorite programming language? ")

if programming_language.lower() == "python":
   print("Excellent choice for AI!")
else:
   print("That's a great language too! Keep learning.")

print("Hello,", name,"." "You are", age, "years old." "You are studying", course, "at the", university, "and your favorite programming language is", programming_language, ".")


#Stretch Challenge

# Ask the user for:

# How many hours do you study per day?

# If:

# 5 or more → "Excellent consistency!"
# 3–4 → "Great job! Keep improving."
# Less than 3 → "Small daily improvements lead to big results."

study_hours = int(input("How many hours do you study per day? "))
if study_hours >= 5:
    print("Excellent consistency!")
elif 3 >= study_hours <= 4:
    print("Great job! Keep improving.")
else:
    print("Small daily improvements lead to big results.")


print("Thank you for using the Student Profile Generator!")