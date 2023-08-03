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