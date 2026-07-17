# Mini Challenge 1

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

books = []

for _ in range(3):
  book = create_book()
  books.append(book)

print(books)