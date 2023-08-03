# 4 
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number.Suppose the following input is supplied to the program:

user_input = input("Enter a sequence of numbers: ")

# Convert the user input into a list of integers
number_list = [int(num) for num in user_input.split()]

# Convert the user input into a tuple of integers
number_tuple = tuple(int(num) for num in user_input.split())

# Print the list and tuple
print("List:", number_list)
print("Tuple:", number_tuple)

# other solution (without coma):

lst = input("Enter a sequence of numbers: ").split(',')  # the input is being taken as string and as it is string it has a built in
                          # method name split. ',' inside split function does split where it finds any ','
                          # and save the input as list in lst variable

tpl = tuple(lst)          # tuple method converts list to tuple

print(lst)
print(tpl)


# Define a class which has at least two methods: (ESTUDAR MAIS)

#getString: to get a string from console input
#printString: to print the string in upper case.
#Also please include simple test function to test the class methods.


class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print("The string in upper case:", self.input_string.upper())

def testStringManipulator():
    # Create an instance of the StringManipulator class
    manipulator = StringManipulator()

    # Test the getString method
    manipulator.getString()

    # Test the printString method
    manipulator.printString()

# Test the class methods
testStringManipulator()

# 6´
# Write a program that calculates and prints the value according to the given formula:

#Q = Square root of [(2 _ C _ D)/H]

#Following are the fixed values of C and H:

#C is 50. H is 30.

#D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

#100,150,180
#The output of the program should be:

#18,22,24

import math

# Fixed values of C and H
C = 50
H = 30

def calculate_Q(D):
    return int(round(math.sqrt((2 * C * D) / H)))

def main():
    input_sequence = input("Enter 3 comma-separated values : ")
    D_values = input_sequence.split(',')

    result = [calculate_Q(int(D)) for D in D_values]

    print(','.join(map(str, result)))

if __name__ == "__main__":
    main()

#Explanation:

"""The program takes the comma-separated input sequence from the user as a string.
It splits the input sequence into a list of individual values using the split() method.
For each value in the D_values list, it calculates the corresponding Q using the given formula.
The calculated Q values are rounded to the nearest integer using int(round()).
The final rounded Q values are then printed in a comma-separated sequence using ','.join(map(str, result)).
This program will produce the correct output based on the given formula and fixed values of C and H."""


# 7
# _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i _ j.*

first_array = []
second_array = []

try:  
    user_input = input("Enter 2 digits separated by coma ")
    int(user_input) 

    user_input[0] = lst
    user_input[1] = number_list 

    # sequence 0 to infinite inside of a list.
    number_list = range

    # Using list comprehension to create a list of empty lists
    lists_container = [[] for _ in range(lst)]
        
    for i in lists_container:
        range * (i + 1)
    print(lists_container)

except ValueError:
    print("Invalid input. Please enter a valid integer.")

# separar os valores em : primeiro valor é número de listas, segundo valor é quantidade de números de 1 a 0 dentro das listas.
# Loop. 