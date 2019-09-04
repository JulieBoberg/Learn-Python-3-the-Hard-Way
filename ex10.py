# defines variable tabby_cat that is a string indented via "\t"
tabby_cat = "\tI'm tabbed in."
# defines variable persian_cat that is a string that contains a line split using "\n"
persian_cat = "I'm split\non a line."
# defines a variable backslash_cat that is a string split up with "\" that are coded with "\\"
backslash_cat = "I'm \\ a \\ cat."

# defines variable fat_cat which is a multiline quote using """
# each line that contains \t is indented
# the last line contains two indentations and a new line split with '\n'
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# prints contents of variable tabby_cat
print(tabby_cat)
# prints contents of variable persian_cat
print(persian_cat)
# prints contents of variable backslash_cat
print(backslash_cat)
# prints mulitiline quote contained in variable fat_cat
print(fat_cat)
