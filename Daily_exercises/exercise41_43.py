# 41

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

squared_numbers_list = list(squared_numbers)

print(squared_numbers_list)

#

numbers = [1, 2, 3, 4, 5]

doubled_numbers = map(lambda x: x * 2, numbers)

doubled_numbers_list = list(doubled_numbers)

print(doubled_numbers_list)



# 42

def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to select even numbers from the list
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Use map() to square each even number
squared_even_numbers = map(square, even_numbers)

# Convert the result to a list (map() returns an iterable)
squared_even_numbers_list = list(squared_even_numbers)

print(squared_even_numbers_list)

#

li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)



# 43

evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)


def even(x):
    return x%2==0

evenNumbers = filter(even, range(1,21))
print(list(evenNumbers))
