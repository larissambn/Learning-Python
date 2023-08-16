import re

while True:

    user_input = input("Enter passwords: ").split(" ")
    passwords = list(user_input)
    is_valid = False

    for password in passwords: 
        if (len(password)) < 6 or len((password)) > 12:
            #print("Not valid! Total characters should be between 6 and 12")
            continue
        elif not re.search("[a-z]",password):
            #print("Not valid! It should contain one letter between [a-z]")
            continue
        elif not re.search("[A-Z]", password):
            #print("Not valid! It should contain one letter between [A-Z]")
            continue
        elif not re.search("[0-9]",password):
            #print("Not valid! It should contain one ldigit between [0-9]")
            continue
        elif not re.search("[$#@]",password):
            #print("Not valid! It should contain at least one character : [$#@]")
            continue
        else:
            is_valid = True
            break
    print("Valid passwords:"+ password + ",")
