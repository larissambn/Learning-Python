# 38

tp = (1,2,3,4,5,6,7,8,9,10)
tp1 = tp[:5]
tp2 = tp[5:]
print (tp1,"\n",tp2)


tup = [i for i in range(1, 11)]
print(f'{tuple(tup[:5])} \n{tuple(tup[5:])}')


tpl = (1,2,3,4,5,6,7,8,9,10)

for i in range(0,5):
    print(tpl[i],end = ' ')
print()
for i in range(5,10):
    print(tpl[i],end = ' ')

# 39

tpl = (1,2,3,4,5,6,7,8,9,10)
tpl1 = tuple(i for i in tpl if i%2 == 0)
print(tpl1)

# 40

text = input("Enter text: ")
if text == "yes" or text == "YES" or text == "Yes":
    print("Yes")
else:
    print("No")