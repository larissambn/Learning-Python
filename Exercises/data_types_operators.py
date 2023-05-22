print('He said  "There are some who call me the Messiah"')
print("He's is the Messiah, he's our savior")

savings = 2500
print("You have" + " " + str(savings) + " " +"in the bank")
print("Your account has", savings, "euros") # coma is a possible way to concatenate integers in a sting phrase

# balance = 350
# deposit = input("Please enter the amount you wish to deposit : ")

# deposit = float(deposit)

temp = 19.99

temp = int(temp)

print("The temparature is", temp, "degrees")

#Exercise 6

watches = ['Compass Watch', 'GPS Watch', 'Stun Watch', 'NerveGas Watch', 'Inflatable Dingy Watch', 'Android Watch', 'Lunchtime Alarm Watch']

watches.append('Jingly Jangly Watch')

watches.remove("Android Watch")

watches.insert(0, "Apple Watch")

print(watches)

print(watches.index("Inflatable Dingy Watch"))

current_watch = watches[5]

print(current_watch)


rations = ["cereals", "Powdered soup", "chocolate", "Trifle"]

rations.sort(key=str.lower)

print(rations)

lunch = rations[-1]

print(lunch)

breakfast_of_champions = rations[0:2]
print(breakfast_of_champions)
 
#Exercise 7

hurdle_time = 9.95
height_from_road = 10.75

unlock_mission = hurdle_time <=10 and height_from_road > 11
unlock_weapon = hurdle_time <=10 or height_from_road > 11
