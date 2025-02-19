#Please explain what it means that a list is mutable and a string is not mutable (imutable).
#Give some code that shows the difference. Use your own words

# Creating a list
my_list = ["apple", "banana", "cherry"]
print("Original List:", my_list)

# Changing an element
my_list[1] = "blueberry"
print("Modified List:", my_list)

# Creating a string
my_string = "hello"
print("Original String:", my_string)

# Trying to change a character (this will cause an error)
try:
    my_string[0] = "H"
except TypeError as e:
    print("Modified String:", e)