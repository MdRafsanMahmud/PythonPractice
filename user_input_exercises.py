# 1. Greeting Program
# Create a simple program that asks for user's name and responds with
# personalized greeting.

user_name = input("Enter your name: ")
print(f"Hello {user_name} , welcome to Python!")

#  2. Echo Machine
# Create a simple program that will promt the user to type somathing and then
# repeat it back exactly as entered.

user_input = input("Enter your full name: ")
print(user_input)

# 3. Favorite Color
# Write a program that inquires about the user's favorite color and responds with
# the comment about that color.

user_color = input("Enter your favorite color: ")
print(f"The color of rose is {user_color}")

# Multiple Inputs
# 4. Create a program that gathers the user's name, age, and hometown, then crafts
# a summary sentence using this information.

user_name1 = input("Enter your name: ")
age = int(input("Enter your age: "))
hometown = input("Enter your hometown: ")
print(f"This is {user_name1}, Age is {age} and Hometown is {hometown}")

# 5. Pet Description
# Write a program that asks for a pet's name, species, and age, then generates
# a sentence describing the pet.

pet_name = input("What is your pet's name? ")
species = input("What is your pet's species: ")
pet_age = input("What is your pet's age: ")
print(f"Short Description of {pet_name}: \nSpecies: {species} \n{pet_age} years old.")

# 6. Travel Planner
# Develop a program that requests a destination, mode of transport, and duration
# of stay, then prints a brief travel plan.

destination = input("Enter destination: ")
transport_mode = input("Transport mode: ")
duration = input("Duration of Stay: ")
print(f"Travel Plan \nDestination: {destination}\nTransport mode: {transport_mode}\nDuration of Stay: {duration}")


# Coverting Input to Integers
# 7. Create a program that asks for the user's age, converts it into integer,
# then calculates and prints their age in 'dogs years' (multiply by 7).

user_age = input("How old are you? ")
dogs_years = int(user_age) * 7
print(f"Your are {user_age} old and Your age in dog years is: {dogs_years}")


# 8. Simple Calculator
# Create a program that prompts for two numbers and operation (+, -, *, /),
# performs the calculation, and displays the result.

first_value = float(input("Enter first value: "))
second_value = float(input("Enter second value: "))
addition = first_value + second_value
subtraction = first_value - second_value
multiplication = first_value * second_value
division = first_value / second_value

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

# 9. Days to Hours
# Develop a program that asks for a number of days, converts it into an integer,
# then calculates and prints the equivalent number in hours.
#
# num_of_days = int(input("Please enter the number of days: "))
# print(f"{num_of_days} days is equivalent to {num_of_days * 24} hours:")


# 10. Mad Libs
# Create a simple Mad Libs game. Ask the user for an adjective, a noun, and a verb,
# then use these inputs to compltete a pre-written sentence.

adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

print(f"The {adjective} {noun} decided to {verb} all day long.")



# 11. Story Generator
# Write a program that requests a character name, a place, and an object, then
# weaves these elements into a short short story.

character = input("Enter a character name: ")
place = input("Enter a place: ")
object_ = input("Enter an object: ")

print(f"\nOnce upon a time in {place}, there lived a brave soul named {character}.")
print(f"One day, {character} discovered a mysterious {object_} hidden deep in the forest.")
print(f"With courage in their heart and the {object_} in hand, {character} set off on an unforgettable adventure.")














