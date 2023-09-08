# 31

def printDict():
    dict={i:i**2 for i in range(1,21)}   
    print(dict)

printDict()

# 32

def printDict():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict.keys())      # print keys of a dictionary

printDict()

# 33

def printList():
    lst = [i ** 2 for i in range(1, 21)]
    print(lst)

printList()

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li)

printList()

# 34

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print(li[:5])

printList()

def printList():
    lst = [i ** 2 for i in range(1, 21)]

    for i in range(5):
        print(lst[i])

printList()

def func():
    print([i**2 for i in range(1,21)][:5])

func()

# 35

def squares(n):
    squares_list = [i**2 for i in range(1,n+1)]
    print(squares_list[-5:])
squares(20)

# 36

def printList():
	li=list()
	for i in range(1,21):
		li.append(i**2)
	print (li[5:])

printList()

def printList():
    lst = [i ** 2 for i in range(1, 21)]
    for i in range(5,20):
        print(lst[i])

printList()

# 37

def printTupple():
    lst = [i ** 2 for i in range(1, 21)]
    print(tuple(lst))

printTupple()


def square_of_numbers():
    return tuple(i ** 2 for i in range(1, 21))

print(square_of_numbers())
