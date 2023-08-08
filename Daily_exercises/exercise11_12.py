# 11

binary_numbers = input("Enter a sequence of binary numbers of 4 digits: ").split(',')
binary_divisible = map(int, binary_numbers)

divisible_by_5 = [num for num in binary_divisible if num % 5 == 0]

print(','.join(map(str, divisible_by_5)))

# 12

for number in range(1000,3001):
    
    digit_1 = number // 1000  # Thousands digit
    digit_2 = (number // 100) % 10  # Hundreds digit
    digit_3 = (number // 10) % 10   # Tens digit
    digit_4 = number % 10  # Ones digit
    
    if digit_1 % 2 == 0 and digit_2 % 2 == 0 and digit_3 % 2 == 0 and digit_4 % 2 == 0 :
        print(number, end=', ')