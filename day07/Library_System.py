# Library Book Management System

# Empty List 
books = []

# Function 1
def add_book(): 
  title = input("What is the book title: ")
  author = input("Who is the author: ")
  year = int(input("What year was it published: "))

  book = {
    "Title": title,
    "Author": author,
    "Year": year
  }
  return book

# Function 2

def display_books(books):
  for book in books:
    print("\n----Library Books--")
    print("Title: ", book["Title"])
    print("Author: ", book["Author"])
    print("Year: ", book["Year"])
    print("-------------------------")

# Step 4

number = int(input("How many books would you like to add? "))

for _ in range(number):
  book = add_book()
  books.append(book)

# step 5
display_books(books)

# Boss Level

search = input("Search a book title: ")

found = False

for book in books:
  if book["Title"].lower() == search.lower():
    print("\nBook Found!")
    print("Title: ", book["Title"])
    print("Author: ", book["Author"])
    print("Year: ", book["Year"])
    found = True
    break
if not found:
  print("Book not found")

# Etra Boss Challenge

another = input("Would you like to add another book? ")

if another.lower() == "yes":
   book = add_book()
   books.append(book)

   print("\nUpdated Library: ")
   display_books(books)
   
elif another.lower() == "no":
  print("Thank you for using the Library Management System.")

else:
  print("Please enter yes or no.")



  