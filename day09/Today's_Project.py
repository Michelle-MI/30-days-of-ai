#Lucky Student Picker
import random

students = [
  "Michelle",
  "Brian",
  "Grace",
  "Kevin",
  "Faith"
]

lucky_student = random.choice(students)
print(f"Today's lucky student is: {lucky_student}")

# Stretch challenge
from random import randint

number = randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
  print("Congratulations!")
else:
  print(f"Wrong! The correct number was {number}.")