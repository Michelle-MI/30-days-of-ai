# Mini Challenge 2

def create_book():
  title = input("What is the name of your book: ")
  author = input("Who is the author: ")
  year = int(input("What year what was it published: "))

  book = {
    "Title": title,
    "Author": author,
    "Year": year
  }
  return book

books = create_book()
print(books)