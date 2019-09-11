from sys import argv

script, input_file = argv

# define function print_all that accepts parameter f(a file)
def print_all(f):
    # read the file(f) and print it
    print(f.read())
# define function rewind which accepts parameter f
def rewind(f):
    # find the (0) start of the file(f)
    f.seek(0)
# define the function print_a_line that accepts line_count and a file(f)
def print_a_line(line_count, f):
    # Goes to line specified in line_count and reads that line of the file, prints
    print(line_count, f.readline())

# variable current_file opens the input_file
current_file = open(input_file)

# prints a string that ends with a line break
print("First let's print the whole file:\n")

# calls function print_all with current_file as parameter. This opens, reads and prints the input_file
print_all(current_file)
# prints a string
print("Now let's rewind, kind of like a tape.")

# calls function rewind that opens the input_file and goes to start of file.
rewind(current_file)
# prints a string
print("Let's print three lines:")

# variable current_line is set to 1
current_line = 1
# calls print_a_line which takes the current_line and prints it from current_file
print_a_line(current_line, current_file)
# variable current_line is increased by 1
current_line = current_line + 1 # current_line += 1
# calls print_a_line again but current_line is increased by 1
print_a_line(current_line, current_file)
# calls print_a_line again but current_line is increased by 1
current_line = current_line + 1 # current_line += 1
print_a_line(current_line, current_file)
