# Mini Challenge 2
#Add a method called:

# display()

# that prints:

# Title:
# Author:

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def display(self):
    print(f"Title: {self.title}")
    print(f"Author: {self.author}")

book = Book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie")
book.display()