# 7 (example)

def generate_2d_array(X, Y):
    # Using nested list comprehension to create the 2-dimensional array
    array_2d = [[i * j for j in range(Y)] for i in range(X)]

    return array_2d

# Example: Generate a 2-dimensional array with 3 rows and 5 columns
result_array = generate_2d_array(9, 3)
print(result_array)

# other solution

user_input = input("Enter 2 numbers separated by comma please: ")
x,y = map(int,user_input.split(','))
lst = [[i*j for j in range(y)] for i in range(x)]
print(lst)

# 8 
user_input = input("Write a sequence of words: ").split(',')
user_input.sort()

# Join the sorted list of words into a comma-separated string
sorted_words = ','.join(user_input)

print(sorted_words)

# 9

lines = []

while True:
    line = input("Enter a line (or write 'quit' to finish): ")
    if line.lower() == 'quit':
        break  # Exit the loop
    lines.append(line)

print("\nYou entered the following lines:")
for line in lines:
    line = line.upper()
    print(line)

