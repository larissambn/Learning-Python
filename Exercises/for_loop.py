original_list = [1,2,3,4,5]
cubes_list = []

for i in original_list:

    cubes_list.append( i ** 3)

print(cubes_list)


market_list = [["apple", "banana", "pear","strawberry","grape"]]
smoothie_list = []

for fruit_list in market_list:
    for fruit in fruit_list:
        smoothie_list.append(fruit)
print(smoothie_list)


leap_year_range =range(2000,2100,4)

leap_year_list = list(leap_year_range)
print(leap_year_list)