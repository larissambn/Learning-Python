# 1
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
#between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

for number in range(2000,3200):
    if number % 7 == 0 and number % 5 != 0 :
        print(number, end=",")
    
# 2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320 (1 * 2 * 3 * 4 * 5 * 6 * 7 * 8)

try:
    user_input = input("Enter a number:  ")
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

# 3 
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
# such that is an integral number between 1 and n (both included). 
# Then the program should print the dictionary.Suppose the following input is supplied to the program: 8
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

user_input = int(input("Enter a number: "))

dictionary = { } # initialize it empty to store key-value pares.

for i in range (1, user_input + 1 ) :  # range inclusive on the first number but not on the last.
    dictionary[i] = i * i # [i] for key and ( i * i ) for value.

print(dictionary)

# 3 - Other solution 

'''Solution by: minnielahoti
   Corrected by: TheNobleKnight 
'''

try:
    num = int(input("Enter a number: "))
except ValueError as err:
    print(err)

dictio = dict()
for item in range(num+1):
    if item == 0:
        continue
    else:
        dictio[item] = item * item
print(dictio)

# 4

