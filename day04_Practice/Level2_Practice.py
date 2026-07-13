# Excercise 4

number = int(input("Enter a number: "))

for i in range(1, 13):
  print(number, "x", i, "=", number * i)


# Excercise 5
name = "Michelle"
count = int(input("How many times should i print your name: "))

for _ in range(count):
  print(name)


# Excercise 6
count = 50
while count >= 0:
  print(count)
  if count % 10 == 0:
    print("Checkpoint!")
  
  count -= 1
  
  