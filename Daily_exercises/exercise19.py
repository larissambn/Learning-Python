lst = []
while True:
    user_input = input().split(',')
    if not user_input[0]:                          # breaks for blank input
        break
    lst.append(tuple(user_input))

lst.sort(key= lambda x:(x[0],int(x[1]),int(x[2])))  # here key is defined by lambda and the data is sorted by element priority 0>1>2 in accending order
print(lst)