# print numbers only if they are not divisible by 7
# print list until it reaches 315.

numbers_list = [92, 25, 27, 453200, 14, 35, 9203, 700, 315, 7, 70, 329, -7]

random_numbers =  [ x for x in numbers_list if x % 7 != 0]
print(random_numbers)

for number in numbers_list:
     if number == 315:
         break
     print(number)

for i in numbers_list:
    if ( i == 315):
        break
    if ( i % 7 == 0):
        continue
    print(i, end = " ")

# Print the cubes of numbers of a random list, only if those numbers are divisible by 3;

original_list = (283792, 4, 21, 24, 49, 14, 35, 9203, 432, 5940549, 700, 315, 329, -7)

cubes =  [ x ** 3 for x in original_list if x % 3 == 0 ]
print(cubes)