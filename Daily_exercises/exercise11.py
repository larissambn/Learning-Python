# 11

binary_numbers = input("Enter a sequence of binary numbers of 4 digits: ").split(',')
binary_divisible = map(int, binary_numbers)

divisible_by_5 = [num for num in binary_divisible if num % 5 == 0]

print(','.join(map(str, divisible_by_5)))
