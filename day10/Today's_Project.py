# Today's Project
#Student Class

# Create a class called:

# Student

# It should have:

# name
# age
#course

# Add a method:

# introduce()

# Output:

# Hello!

# My name is Michelle.

# I am 23 years old.

# I study Computer Science.

# Create three students and call introduce() for each.

class Student:
  def __init__(self, name, age, course):
    self.name = name
    self.age = age
    self.course = course

  def introduce(self):
    print(f"My name is {self.name}.")
    print(f"I am {self.age} years old.")
    print(f"I study {self.course}.")

student1 = Student("Michelle", 23, "Computer Science")
student2 = Student("Brian", 22, "Software Engineering")
student3 = Student("Grace", 24, "Artificial Intelligence")

student1.introduce()
student2.introduce()
student3.introduce()

# Stretch Challenge
# Create a class called:

# BankAccount

# It should store:

# account holder
# balance

# Add methods:

# deposit(amount)
# withdraw(amount)
#display_balance()

# Example:

# Deposit: 500

# Current Balance: 1500

class BankAccount:
  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposit: {amount}")

  def withdraw(self, amount):
    self.balance -= amount
    print(f"Withdraw: {amount}")

  def display_balance(self):
    print(f"Current Balance: {self.balance}")

account1 = BankAccount("Michelle", 2000)
account2 = BankAccount("Brian", 1500)
account3 = BankAccount("Grace", 3000)

account1.deposit(1000)
account1.display_balance()