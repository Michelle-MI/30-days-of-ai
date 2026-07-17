# Today's project - Student Manager

students = ["Michelle", "Brian", "Grace"]
print("Current students: ", students)

name = input("Enter a new student: ")
students.append(name)
print("Updated students: ", students)
print("Total students: ", len(students))

# Stretch Challenge

favorite_tvseries = ["Fringe", "Castle", "Elementary"]
favorite = input("Enter one of your favorites: ")
favorite_tvseries.append(favorite)

remove =input("Which tv series would you like to remove? ")
favorite_tvseries.remove(remove)

print(favorite_tvseries)