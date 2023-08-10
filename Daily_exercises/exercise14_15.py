sentence = input("Enter a sentence: ")

lower_case = 0
upper_case = 0

for char in sentence:
    if char.islower():
        lower_case += 1
    elif char.isupper():
        upper_case += 1

print("LOWER CASE:", lower_case)
print("UPPER CASE:", upper_case)

# other solution

word = input()
upper = sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))

# 15

num = input("Enter a number: ")

sum = num, num * 2, num * 3, num * 4 # multiply them as strings

number_list = [int(i) for i in sum] # turn the strings into integer

total_sum = number_list[0] + number_list[1] + number_list[2] + number_list[3] # sum them all

print(total_sum)

# other solutions 

a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)