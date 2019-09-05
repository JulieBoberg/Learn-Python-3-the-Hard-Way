from sys import argv

#script, first, second, third = argv

#print("This script is called:", script)
#print("Your first variable is:", first)
#print("Your second variable is:", second)
#print("Your third variable is:", third)


# write script that takes argv and input()

# in powershell I run this as Python ex13(script) Julie(name)
script, name = argv
# prints the name of the script
print("This script is called: ", script)
#prints the name entered
print("My name is: ", name )
# asks for input to be stored in variable hobby
hobby = input("My hobby is: ")
# prints an fstring including argv info and input 
print(f"My name is {name} and my hobby is {hobby} and I am working on {script}")
