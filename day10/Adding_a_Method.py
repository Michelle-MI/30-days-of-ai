class Student:
  def __init__(self, name, course):
    self.name = name
    self.course = course

  def introduce(self):
    print(f"My name is {self.name}.")
    print(f"I study {self.course}.")

student = Student("Michelle", "Computer Science")
student.introduce()