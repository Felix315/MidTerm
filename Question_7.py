# Here si some code:

# import random
# random_numbers = []
# for i in range(10):
#    random_numbers.append(random.randint(1, 100))
# continue here

# Continue by removing the odd numbers from the list.
# Also replace the even numbers with their double value
# print the list at the end
#Use only what we have learned in class. Provide some explanation in the form of comments.

import random

# Create an empty list to store random numbers
random_numbers = []

# Generate 10 random numbers between 1 and 100
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Print the original list
print("Original list:", random_numbers)

# Create a new list to store only even numbers (removing odd numbers)
even_numbers = []

for num in random_numbers:
    if num % 2 == 0:  # Check if the number is even
        even_numbers.append(num * 2)  # Double the even numbers

# Print the modified list
print("Modified list (even numbers doubled):", even_numbers)