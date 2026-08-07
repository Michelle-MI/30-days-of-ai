# Today's Challenge
# Create: countdown.py
#Requirements:

# Ask the user for a starting number.
#Count down to zero.

#Example:

#Enter starting number: 5
5,4,3,2,1,0

#Blast off! 🚀

# Use a while loop.

number = int(input("Enter the starting number: "))

count = number

while count >= 0:
 print(count)
 count -=1

print("Blast off! ")

# Stretch challenge
# Build a multiplication table.

# Ask the user for a number.

#If they enter: 7

# Print:

# 7 × 1 = 7
# 7 × 2 = 14
...
# 7 × 10 = 70

# Use a for loop.

number = int(input("Enter a number: "))

for i in range(1, 11):
 print(number, "x", i, "=", number * i)

