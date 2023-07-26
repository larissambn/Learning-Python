#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

for number in range(2000,3200):
    if number % 7 == 0 and number % 5 != 0 :
        print(number, end=",")

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320 (1 * 2 * 3 * 4 * 5 * 6 * 7 * 8)

try:
    user_input = input("Enter a number: ")
    number = int(user_input)

    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i

        print("The factorial of your number is:", factorial)

except ValueError:
    print("Invalid input. Please enter a valid integer.")