class Student:
  def __init__(self, name, course):
    self.name = name
    self.course = course

# Creating Objects
student1 = Student("Michelle", "Computer Science")
student2 = Student("Brian", "Software Engineering")

# Accessing Data
print(student1.name)
print(student2.course)