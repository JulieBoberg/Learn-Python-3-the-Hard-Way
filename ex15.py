from sys import argv
# set variable argv to script and filename to be entered when running script
script, filename = argv
# set variable text to function open with the parameter filename.
txt = open(filename)
# prints an f-string "Here's your " and contains the filename
print(f"Here's your {filename}: ")
# prints the text from the file that is opened in variable txt
print(txt.read())
# a prompt to type the filename again.
print("Type the filename again:")
# set input to variable file_again
file_again = input("> ")
# variable txt_again is set to open the file taken as input for variable file_again
txt_again = open(file_again)
# prints the text of the file
print(txt_again.read())
