# Students Records File Manager

with open("students.txt","a") as file:
  while True: 
   name = input("What is your name: ")
   course = input("What course are you enrolled in: ")
   file.write(f"{name} - {course}\n")
   another = input("\nWould you like to add another student? (yes/no)\n")
   if another.lower() != "yes":
     break

view = input("Would you like to view all students? ")

if view.lower() == "yes":
    try:
        with open("students.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No student records found.")