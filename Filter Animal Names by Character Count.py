# Task: Categorize Animals by Name Length
# Create a program that goes through a list of animal names.
# If the name is longer than 10 characters, categorize it as a "long" name.
# Otherwise, categorize it as a "short" name.
# Print both categories separately with proper formatting.

animals = [
    "Jaguar",
    "Elephant",
    "Crocodile",
    "Chimpanzee",
    "Hedgehog",
    "Alligator",
    "Kangaroo",
    "Hippopotamus",
    "Rhinoceros",
    "CaliforniaCondor"
    ]
short_animals = ""
long_animals = ""
for animal in animals:
    if len(animal) > 10:
        short_animals += "\n" + animal
    else:
        long_animals += "\n" + animal
print(f"\nList of short named animals: {short_animals}")
print(f"\nList of long names animals: {long_animals}")