# declare variable formatter and set it equal to a string with four sets of brackets.
formatter = "{} {} {} {}"
# prints the string in the variable formatter with the arguments in format in place of the brackets
print(formatter.format(1, 2, 3, 4))
# prints the string in the variable formatter with the arguments in format in place of the brackets
print(formatter.format("one", "two", "three", "four"))
# prints the string in the variable formatter with the arguments in format in place of the brackets
print(formatter.format(True, False, False, True))
# prints the string in the variable formatter and each bracket contains the entire string of formatter
print(formatter.format(formatter, formatter, formatter, formatter))
# prints formatter with each bracket replaced by a string provided in format()
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
