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

lst = input("Enter a sequence of numbers").split(',')  # the input is being taken as string and as it is string it has a built in
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

# 5


