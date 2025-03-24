my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert 15 at index 1 (second position)
my_list.insert(1, 15)

# Extend the list by adding multiple elements
my_list.extend([50, 60, 70])

# Remove the last element (70) using pop()
my_list.pop()

# Sort the list in ascending order
my_list.sort()

# Find the index of the value 30 and print it
index_30 = my_list.index(30)
print("Index of 30:", index_30)
