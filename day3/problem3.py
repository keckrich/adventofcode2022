# X = [l.strip() for l in open('in\\3.txt')]
# # XS = [int(x) for x in open('1.in')]

# sum = 0 

# for x in X:
#     a, b = x[:len(x)//2], x[len(x)//2:]
#     c=(set(a)&set(b)).pop()
#     if ord(c) < 97:
#         sum += ord(c) - 38
#     else:
#         sum += ord(c)-96

# print(sum)

# sum = 0 

# for x in range(0,len(X),3):
#     c=list(set(X[x])&set(X[x+1])&set(X[x+2]))[0]
#     if ord(c) < 97:
#         sum += ord(c) - 38
#     else:
#         sum += ord(c)-96

# print(sum)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# X = [l.strip() for l in open('in\\3.txt')]

# # Initialize sums to 0
# sum1 = 0 
# sum2 = 0

# # Loop over the elements in X
# for x in X:
#     # Split the element into two substrings
#     a, b = x[:len(x)//2], x[len(x)//2:]

#     # Find the common characters in a and b
#     c = (set(a) & set(b)).pop()

#     # Calculate the first sum based on the character's ASCII value
#     if ord(c) < 97:
#         sum1 += ord(c) - 38
#     else:
#         sum1 += ord(c) - 96

# # Use a list comprehension to calculate the second sum
# sum2 = sum([ord(list(set(X[x]) & set(X[x+1]) & set(X[x+2]))[0]) - 38 if ord(list(set(X[x]) & set(X[x+1]) & set(X[x+2]))[0]) < 97 else ord(list(set(X[x]) & set(X[x+1]) & set(X[x+2]))[0]) - 96 for x in range(0, len(X), 3)])

# # Print the final sums
# print(sum1)
# print(sum2)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # Parse the input
# rucksacks = [l.strip() for l in open('in\\3.txt')]

# # Create a dictionary to keep track of the frequency of each item type
# item_frequencies = {}

# # Loop through each rucksack
# for rucksack in rucksacks:
#     # Find the length of each compartment
#     compartment_length = len(rucksack) // 2
    
#     # Get the items in the first and second compartment
#     first_compartment = rucksack[:compartment_length]
#     second_compartment = rucksack[compartment_length:]
    
#     # Loop through each character in the first compartment
#     for char in first_compartment:
#         # Check if the character also appears in the second compartment
#         if char in second_compartment:
#             # If it does, increment its frequency in the dictionary
#             if char in item_frequencies:
#                 item_frequencies[char] += 1
#             else:
#                 item_frequencies[char] = 1

# # Calculate the sum of the priorities of the item types that appear in both compartments
# sum_of_priorities = 0

# for item, frequency in item_frequencies.items():
#     # Skip this item if it does not appear in both compartments of every rucksack
#     if frequency != len(rucksacks):
#         continue
    
#     # Get the priority of the item type
#     if item.islower():
#         priority = ord(item) - ord('a') + 1
#     else:
#         priority = ord(item) - ord('A') + 27
    
#     # Add the priority to the sum
#     sum_of_priorities += priority

# # Print the sum of the priorities
# print(sum_of_priorities)