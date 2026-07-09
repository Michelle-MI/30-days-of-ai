# Today's Project

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


study_hours = int(input("How many hours do you study per day? "))
if study_hours >= 5:
    print("Excellent consistency!")
elif 3 >= study_hours <= 4:
    print("Great job! Keep improving.")
else:
    print("Small daily improvements lead to big results.")


print("Thank you for using the Student Profile Generator!")