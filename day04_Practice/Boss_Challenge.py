# Study Session Tracker

name = input("What is your name: ")
sessions = int(input("How many study sessions per week have you completed: "))
total_hours = 0

for session in range(1, sessions + 1):
  hours = int(input(f"How many hours did you study in session {session}? "))
  total_hours += hours

print("Total study hours:", total_hours)

if total_hours >= 20:
    print("Outstanding effort!")
elif total_hours >= 10:
    print("Great consistency!")
else:
    print("Let's aim for a little more next week.")
