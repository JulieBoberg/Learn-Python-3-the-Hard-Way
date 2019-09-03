# Declaring the variable cars which contains the number 40
cars = 100
# Declaring the variable space_in_a_car which contains the number 4.0
space_in_a_car = 4.0
# Declaring the variable drivers which contains the number 30
drivers = 30
# Delcaring passengers to contain 90
passengers = 90
# The variable cars_not_driven contains the cars(variable equal to 100) minus drivers(variable equal to 30)
cars_not_driven = cars - drivers
# The variable cars_driven is equal to the variable drivers (which is equal to 30)
cars_driven = drivers
# The variable carpool_capacity now contains the result of multiplying the variable cars_driven by space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
# The variable average_passengers_per_car now equals the number of passengers divided by the number of cars_driven
average_passengers_per_car = passengers / cars_driven

# prints the sentence "There are 100 cars available"
print("There are", cars, "cars available.")
# Prints the sentence "There are only 30  drivers available"
print("There are only", drivers, "drivers available.")
# Prints the sentence "There will be 70 empty cars today."
print("There will be", cars_not_driven, "empty cars today.")
# Prints "We can transport 120.0  people today"
print("We can transport", carpool_capacity, "people today.")
# Prints "We have 90 to carpool today."
print("We have", passengers, "to carpool today.")
# Prints "We need to put about 3.0 in each car."
print("We need to put about", average_passengers_per_car,
 "in each car.")
