# Mini Challenge 1
# Create a class called:

# Book

# Each book should have:

# title
# author

# Create one object.

# Print its title.

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

book = Book("Half of a Yellow Sun", "Chimamanda Ngozi Adichie")
print(book.title)