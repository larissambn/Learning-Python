
# While 
capital = 'Cairo'
answer = ''

while answer != capital: 
    answer = input("What's the capital of Egypt?")

if (answer == capital): 
    print('You won!!')
elif (answer == "quit"):
    print('You gave up!')
else:
    print(answer)


# Class answer

response  = ""

while True :

    response = input("Whats the capital of Egypt?")

    if response == "quit":
        print("The correct answer is Cairo")
        break 

    if response.upper() == "CAIRO":
        print( "You won! ")
        break

    else: 
        print("That is not correct, try again")