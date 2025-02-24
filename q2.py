# Create a new set from unique items from two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
unique_items = set1 ^ set2  # Using ^ operator for symmetric difference
print(unique_items)  # Output: {1, 2, 3, 6, 7, 8}
