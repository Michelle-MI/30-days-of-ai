# Reading from a file

with open("students.txt", "r") as file:
  content = file.read()

print(content)