numbers = input("Enter a sequence of numbers: ")

# Convert the input to a list of integers
numbers_list = [int(num) for num in numbers.split()]

for number in numbers_list:
    if number % 2 != 0:
        number  = number * number
        print(number, end = ", ")
    else:
        pass

# or

squared_odd_numbers = [str(number * number) for number in numbers_list if number % 2 != 0]

# Print the result as a comma-separated string
print(','.join(squared_odd_numbers))

# 17

withdraw = [] 
deposit = []

while True:
    user_input = input("Write W for Withdraw or D for Deposit and select the quantity, enter 'stop' to finish: ")
    
    if user_input.lower() == "stop":
        break
    
    action, amount = user_input.split()
    amount = int(amount)
    
    if action == "W":
        withdraw.append(amount)
    elif action == "D":
        deposit.append(amount)
    else:
        print("Please enter a valid answer within the format")
        continue

sum_withdraw = sum(withdraw)
sum_deposit = sum(deposit)

total = sum_deposit - sum_withdraw

print("Total balance:", total)
