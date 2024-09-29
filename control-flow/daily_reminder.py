task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = ""
match priority:
    case "high":
        print(f"reminder:'{task}' is a high priority task")
    case "medium":
      print( f"reminder:'{task}' is a medium priority task")
    case "low":
         print(f"reminder:'{task}' is a low priority task")
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
if time_bound == "yes":
     print(f"reminder:(reminder)that requires immediate attention today!")
elif time_bound == "no":
    print(f"note:(reminder)Consider completing it when you have free time.")
else:
    print("Invalid input for time-bound. Please enter yes or no.")
print(reminder_message)
