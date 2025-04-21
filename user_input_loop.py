# Tasks
# Use a while loop to continually ask the user to input a word, until
# they type "quit". Once they type a word in, add it to a list. Once they create
# the loop use a for loop to output  the items

names = []
while True:
    name = input("Enter a name: ")
    if name == 'quit':
        break
    names.append(name)
print(f"Names: {names}")