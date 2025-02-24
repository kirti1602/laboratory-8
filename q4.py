# Check if two sets have any elements in common
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
common_elements = set1 & set2  # Using & operator for intersection
if common_elements:
    print("Common elements:", common_elements)  # Output: Common elements: {4, 5}
else:
    print("No common elements")
