# Mini Challenge 1

with open("favorite_movies.txt", "w") as file: 
  file.write("Castle\n")
  file.write("Fringe\n")
  file.write("His Dark Materials\n")

with open("favorite_movies.txt", "r") as file: 
  content = file.read()

print(content)