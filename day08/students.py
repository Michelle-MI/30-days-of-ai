# Writing to a file

with open("students.txt", "w") as file:
  file.write("Michelle\n")
  file.write("Brian\n")
  file.write("Grace\n")

print("Students saved successfully!")