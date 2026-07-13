# Excercise 7

secret = 7
attempts = 1
guess = int(input("Guess the number: "))

while guess != secret:
  print("Wrong!")
  attempts += 1
  guess = int(input("Guess the number: "))

print("Correct!")

print("You guessed it in", attempts, "attempts!")


# Excercise 8
for _ in range(1):
  print("*")
for _ in range(1):
  print("**")
for _ in range(1):
  print("***")
for _ in range(1):
  print("****")
for _ in range(1):
  print("*****")


