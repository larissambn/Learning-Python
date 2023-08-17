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
