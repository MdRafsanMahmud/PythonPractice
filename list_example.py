# Managing a shopping list and grocery items
# 1. Checking if an itme is in the list
# 2. Adding an item to the list
# 3. Removing an item from the list
# 4. Accessing an item by index
# 5. Modifying the quantity of an item in the nested grocery list


# 1. Checking if an itme is in the list
shopping_list = ['milk', 'eggs', 'bread', 'rice']
print(f"Shopping List: {shopping_list}")

item_to_check = input("What item would you like to check? ")
for item in shopping_list:
    if item == item_to_check:
        print(f"{item_to_check.capitalize()} is in the shopping list.")
        break
else:
    print(f"{item_to_check} is not in the shopping list.")


# 2. Adding an item to the list
new_item = input("What item would you like to add? ")
shopping_list.append(new_item)
print(f"Shopping List: {shopping_list}")

# 3. Removing an item from the list
item_to_remove = input("What item would you like to remove? ")
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print(f"Shopping List: {shopping_list}")
    print(f"{item_to_remove} has been removed from the shopping list.")
    print(f"Current shopping list: {shopping_list}")
else:
    print(f"{item_to_remove} is not in the shopping list.")
    print(f"Current shopping list: {shopping_list}")

# 4. Accessing an item by index
index_to_access = int(input("What index would you like to access? "))
try:
    item_at_index = shopping_list[index_to_access]
    print(f"Item at index {index_to_access}: {item_at_index}")
except IndexError:
    print(f"There is no item at index {index_to_access}.")


