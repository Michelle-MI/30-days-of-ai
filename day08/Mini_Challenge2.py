# Mini Challenge 2

with open("languages.txt", "a") as file:
  favorite_language = input("What is your favorite programming language: ")
  file.write(favorite_language + "\n")

with open("languages.txt","r") as file:
  content = file.read()

print(content)