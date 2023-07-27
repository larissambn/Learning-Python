# 4 
user_input = input("Enter a sequence of numbers: ")

# Convert the user input into a list of integers
number_list = [int(num) for num in user_input.split()]

# Convert the user input into a tuple of integers
number_tuple = tuple(int(num) for num in user_input.split())

# Print the list and tuple
print("List:", number_list)
print("Tuple:", number_tuple)
