name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Convert inches to centimeters
def centimeters(x):
 total = x * 2.54
 return total
# Convert pounds to kilos
def kilograms(y):
    total = y / 2.205
    return total

print(f"Let's talk about {name}.")
# added in the conversion of inches to centimeters
print(f"He's {height} inches tall or {centimeters(height)} centimeters tall.")
# added in conversion from pounds to kilograms
print(f"He's {weight} pounds heavy or {kilograms(weight)} kilograms.")
print("Actually that's not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

    # this line is trick, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
