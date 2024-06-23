# -----------------------------------------------------------
# Lists and Tuples Tutorial
# -----------------------------------------------------------
# This section explores the use of lists and tuples in Python.
# Lists are mutable sequences of values, while tuples are immutable.

# -----------------------------------------------------------
# Working with Lists
# -----------------------------------------------------------

# Initializing a list of courses
courses = ["BSIT", "BSIS", "BSCS", "BSMT", "BSST", "BSIS"]

# Index explanation for clarity
# Index      0       1       2       3      4      5
# Index     -6      -5      -4      -3     -2     -1

# Accessing elements in the list
print(courses[0])  # Outputs the first element: 'BSIT'
print(courses[-1]) # Outputs the last element: 'BSIS'
print(courses[1:4])# Outputs a slice from index 1 to 3: ['BSIS', 'BSCS', 'BSMT']
print(courses[2:]) # Outputs from index 2 to the end: ['BSCS', 'BSMT', 'BSST', 'BSIS']
print(courses[:5]) # Outputs from the start to index 4: ['BSIT', 'BSIS', 'BSCS', 'BSMT', 'BSST']

# Changing an element in the list
courses[0] = "Hatdog"  # Changes the first element to 'Hatdog'
print(courses)         # Outputs the modified list

# Getting the length of the list
print(len(courses))  # Outputs the length: 6

# Counting occurrences of a specific value
print(courses.count("BSIS"))  # Outputs the count of 'BSIS': 2

# Adding elements to the list
courses.append("Hatdog")     # Appends 'Hatdog' to the end of the list
courses.append("Cheesedog")  # Appends 'Cheesedog' to the end of the list
courses.insert(2, "Corndog") # Inserts 'Corndog' at index 2

print(courses)  # Outputs the list after additions

# Removing elements from the list
courses.remove("Hatdog")  # Removes the first occurrence of 'Hatdog'
print(courses)            # Outputs the list after removal
courses.pop()             # Removes the last element
print(courses)            # Outputs the list after popping the last element
courses.pop(1)            # Removes the element at index 1
print(courses)            # Outputs the list after popping element at index 1

# Deleting elements using the del keyword
del courses[0]  # Deletes the first element
print(courses)  # Outputs the list after deletion

# Commented out deletion of the entire list for safety
# del courses  # Uncommenting this line would delete the entire list

# Clearing all elements from the list
# courses.clear()  # Uncomment to clear all elements in the list
# print(courses)   # Outputs an empty list: []

# Copying a list
coursesCopy = courses.copy()  # Creates a copy of the list
print(coursesCopy)            # Outputs the copied list

# Concatenating lists
print(courses + coursesCopy)  # Outputs concatenated lists

# Extending a list with another list
courses.extend(coursesCopy)   # Extends the list with elements from the copied list
print(courses)                # Outputs the extended list

# Reversing the list
courses.reverse()  # Reverses the list in place
print(courses)     # Outputs the reversed list

# Sorting the list
courses.sort()             # Sorts the list in ascending order
print(courses)             # Outputs the sorted list
courses.sort(reverse=True) # Sorts the list in descending order
print(courses)             # Outputs the list sorted in descending order

# Nested lists
nested_list = ["BSIT", "BSIS", ["Hatdog", "Cheesedog"]]
print(nested_list)        # Outputs the nested list
print(nested_list[2])     # Outputs the nested list within the list
print(nested_list[2][1])  # Outputs 'Cheesedog' from the nested list

# -----------------------------------------------------------
# Working with Tuples
# -----------------------------------------------------------

# Tuples are immutable sequences, meaning they cannot be modified after creation.
coursesTuples = ("BSIT", "BSCS", "BSIS")
print(coursesTuples)  # Outputs the tuple

# Converting between lists and tuples
courses = list(coursesTuples)  # Converts the tuple to a list
print(courses)                 # Outputs the list version of the tuple
courses = tuple(courses)       # Converts the list back to a tuple
print(courses)                 # Outputs the tuple version of the list
