# 12

user = input("Enter a sequence of letters and digits :").split(" ") # split the strings
print(user) 

number_counting = [] 

for i in user: # loop to find numbers in the user input
    try:                #filter the possibility 
        number = int(i) # turn the strings of numbers into numbers.
        number_counting.append(number) # save into a list of integers
    except ValueError:
        pass 

print(number_counting)

#

s_again = list(map(str, number_counting)) # stringify the list of numbers 
print(s_again)

#

count_digits = 0 # Initialize 0 to keep track of the sum of lengths

for st in s_again: 
    st_count = len(st)
    count_digits =+ st_count # Accumulate the lengths

# Count the letters 

letters_count = 0  # Initialize 0 to keep track of the sum of lengths

for j in user:
    count = len(j)
    letters_count += count  # Accumulate the lengths


# print everything
print("DIGITS:", count_digits)
print("LETTERS:", letters_count)
    

# Better version of my code: 

user = input("Enter a sequence of letters and digits: ").split()  # No need to specify the separator

number_counting = [int(i) for i in user if i.isdigit()]  # Using list comprehension

s_again = list(map(str, number_counting))

count_digits = sum(len(st) for st in s_again)  # Using generator expression and sum()

letters_count = sum(len(j) for j in user)

print("DIGITS:", count_digits)
print("LETTERS:", letters_count)

# Simplier solution : 

sentence = input("Enter a sentence: ")

letters_count = 0
digits_count = 0

for char in sentence:
    if char.isalpha():
        letters_count += 1
    elif char.isdigit():
        digits_count += 1

print("LETTERS", letters_count)
print("DIGITS", digits_count)
