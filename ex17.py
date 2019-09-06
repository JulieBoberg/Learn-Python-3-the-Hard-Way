from sys import argv
# import exists which checks existance of files
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read()

# prints an f-string which includes the lenght of indata
print(f"The input file is {len(indata)} bytes long")
# prints and f-string and checks that to_file exists. Returns boolean value
print(f"Does the output file exist? {exists(to_file)}")

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
# closes files
out_file.close()
in_file.close()
