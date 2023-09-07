# 26 

def Sum2(num1, num2):
	return num1 + num2

print(Sum2(1,2))

#OR

sum = lambda n1,n2 : n1 + n2      
print(sum(4,5))

# 27

conv = lambda x : str(x)
n = conv(10)
print(n)
print(type(n))            # checks the type of the variable

# 28

sum = lambda s1,s2 : int(s1) + int(s2)
print(sum("10","45"))      # 55

def printValue(s1,s2):
	print (int(s1) + int(s2))
printValue("3","4") #7

# 29 

sum = lambda s1,s2 : s1 + s2
print(sum("13","34"))        

def printValue(s1,s2):
	print(s1 + s2)

printValue("3","4") #34

# 30

user_input = input("Enter a sequence of 2 words, between spaces : ")
first, second = user_input.split()

if len(str(first)) > len(str(second)):
    print(first)
elif len(str(second)) > len(str(first)):
    print(second)
else:
    print(first, second, end="\n")

# SAME 

user_input = input("Enter a sequence of 2 words, separated by spaces: ")
first, second = user_input.split()

print(max(first, second, key=len))

#OR

func = lambda a,b: print(max((a,b),key=len)) if len(a)!=len(b) else print(a+'\n'+b)
