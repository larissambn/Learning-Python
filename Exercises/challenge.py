age = ""
members = ""
not_allowed  = age > 12
teen = age >= 12 and age <= 17
adult = age >= 18
capacity = range(5)
free_capacity = True

members = int(input("How old are you?"))

for not_allowed in members: # loop does not iterate trough an integer (members). It should be an if statement instead.
    print("You are not allowed")

for adult in members: # same error as above, so it should be an if statement.
    'Here is your ticket, enjoy the ride' if free_capacity else 'You need to wait' # string with no action associated with it. So it should be replaced with a print statement to display the apropriate message.

for teen in members: 
    document = bool(input("Do you have the IdCard?"))
    idCard = True # incorrect logic. Insted of True to ID card it should be a variable called "document"
    auth = 'You can come in' if idCard else 'You need the IdCard',document
    print(auth)

    while True: 

        ride = int(input("How many rides you had?"))
    
        while(ride > 3):
            print("That is not possible, as teens can only go into 3 rides" ,ride)

        if ride == 3:
            print("Warning! You could be sick. But Enjoy your last ride, yout ticket number is: ", str(ride) )
            break 

        if ride == 0:
            print("You still have 3 rides available, enjoy!")
            break

        else:
            print("You got it! Your ticket number is :", str(ride))


    