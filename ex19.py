def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# print string
print("We can just give the function numbers directly:")
# calls function cheese_and_crackers
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
# declares variables amount_of_cheese and amount_of_crackers
amount_of_cheese = 10
amount_of_crackers = 50

# calls function cheese_and_crackers with the declared variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
# calls function
cheese_and_crackers(10 + 20, 50 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# write new function and run 10 dif ways
def your_name(name):
    print(f"Hello, {name}!")
# 1
your_name(input("What's your name: "))
# 2
your_name("Julie")

# 3
name = "Julie"
your_name(name)

# 4
print("I don't think we've met before!")
name = input("What's your name?: ")
your_name(name)


# 5 call your_name within another function
def what():
    print("Hello, what's your name?")
    name = input()
    your_name(name)
what()

# 6


# 7

# 8

# 9

# 10
