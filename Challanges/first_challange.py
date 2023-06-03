# 1st option of correction: 

MAX_CAPACITY = 5
MIN_AGE = 12
MAX_AGE = 17
MAX_MINOR_RIDES = 3

def sell_ticket():
    age = int(input("Enter the age of the person: "))
    if age < MIN_AGE:
        print("Sorry, SpookTrain is not allowed for children under 12 years old.")
    elif age >= MIN_AGE and age <= MAX_AGE:
        school_id = input("Has the person presented their school ID card? (Y/N): ")
        if school_id == 'Y':
            rides = int(input("Enter the number of previous rides on SpookTrain: "))
            if rides < MAX_MINOR_RIDES:
                print("Ticket sold. Enjoy your ride!")
                if rides == MAX_MINOR_RIDES - 1:
                    print("Attention: This is your final ride. Be cautious of possible nausea.")
            else:
                print("Sorry, the person has already reached the maximum number of rides on SpookTrain.")
        else:
            print("Sorry, school ID card is required for minors between 12 and 17 years old.")
    else:
        if MAX_CAPACITY > 0:
            print("Ticket sold. Enjoy your ride!")
        else:
            print("Sorry, SpookTrain is currently at full capacity.")

sell_ticket()

# 2nd option of correction 

def spooktrain_ticket_sales():
    capacity = 5
    rides_allowed = 3

    age = int(input("Enter the age of the person: "))

    if age < 12:
        print("Sorry, children under 12 are not allowed to ride the SpookTrain.")
        return

    if age >= 12 and age <= 17:
        school_id_presented = input("Has the school ID card been presented? (Y/N): ")
        if school_id_presented != "Y":
            print("School ID card is required for minors between 12 and 17.")
            return
        rides_taken = int(input("Enter the number of previous rides: "))
        if rides_taken >= rides_allowed:
            print("This is your final ride. Warning: You could be sick!")
        else:
            print("Enjoy your ride!")
        return

    if capacity > 0:
        print("Enjoy your ride!")
        return
    else:
        print("Sorry, the SpookTrain is currently at full capacity.")

spooktrain_ticket_sales()
