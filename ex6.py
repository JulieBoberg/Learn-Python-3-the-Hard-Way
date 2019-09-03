# declare the variable types_of_people to equal the integer 10
types_of_people = 10
# declare variable x to equal an f-string
x = f"There are {types_of_people} types of people."
# declare variable binary to equal the string 'binary'
binary = "binary"
# declare the variable do_not equal the string "don't"
do_not = "don't"
# declare the variable y to equal an f-string that contains two formated variables
y = f"Those who know {binary} and those who {do_not}."
# prints variable x
print(x)
# prints variable y
print(y)
# prints an f-string that contains variable x
print(f"I said: {x}")
# prints an f-string that contains variable y
print(f"I also said: '{y}'")
# declare variable hilarious to equal boolean value of false
hilarious = False
# declare variable joke_evaluation to equal a string with an embedded variable that has not been formatted
joke_evaluation = "Isn't that joke so funny?! {}"
# prints joke_evaluation and formats it to contain the variable hilarious
print(joke_evaluation.format(hilarious))
# declares variable w to equal a string
w = "this is the left side of..."
# declares variable y to equal a string.
e = "a string with a right side."
# prints concatenated variables w and e
print(w + e)
