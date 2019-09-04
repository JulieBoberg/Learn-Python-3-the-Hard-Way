# variable age stores the value of the user input to the printed string "How old are you?"
age = input("How old are you? ")
# variable height stores the user input to the printed string of "How tall are you?"
height = input("How tall are you? ")
# variable weight stores the user input to the printed string "How much do you weigh?"
weight = input("How much do you weigh? ")

# prints an f-string which inserts the user input into the string via the declared variables.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
