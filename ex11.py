# prints the string "How old are you" with a space at the end.
print("How old are you?", end = ' ')
# variable age is set to users input
age = input()
# prints the string "How tall are you?" with a space at the end.
print("How tall are you?", end = ' ')
# variable height is set to user input
height = input()
# prints "How much do you weigh?" with a space at the end.
print("How much do you weigh?", end = ' ')
# variable weight is set to user input
weight = input()
# prints an f-string that prints the user input for variables age, height & weight within the string.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
