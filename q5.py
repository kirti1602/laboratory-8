# Update set1 by adding items from set2, except common items
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1.update(set2 - set1)  # Using update with the difference of set2 and set1
print(set1)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
