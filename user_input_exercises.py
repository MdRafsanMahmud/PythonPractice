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


















