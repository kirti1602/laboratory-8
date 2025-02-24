# Update the first set with items that don’t exist in the second set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set1 -= set2  # Using -= to subtract elements of set2 from set1
print(set1)  # Output: {1, 2, 3}
