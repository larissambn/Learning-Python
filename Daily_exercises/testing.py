
num = input("Enter a number: ")

sum = num, num * 2, num * 3, num * 4 # multiply them as strings

number_list = [int(i) for i in sum] # turn the strings into integer

total_sum = number_list[0] + number_list[1] + number_list[2] + number_list[3] # sum them all

print(total_sum)

