from sys import argv
# added in extra argument
script, user_name, age = argv
# changed prompt from '> ' to '... '
prompt = '... '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You are {age} years old.
And you have a {computer} computer. Nice.
""")
