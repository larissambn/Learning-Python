kitty = 500
requests = ()
absolute_path = r'C:\Users\laris\Documents\Python_classes\Learning-Python\Assessment2\loan_requests.txt'

with open(absolute_path, 'r+', encoding='utf-8') as f:
    lines = f.readlines()

    print(lines)

requests = [int(i.strip()) for i in lines if i.strip()]

print(requests)

for request in requests:
    with open(absolute_path, "a") as f:
        if kitty == 0:
            print("Request of", request, "is UNPAID!")
            f.write(f"Outstanding request: {request}\n")
        elif kitty > request:
            print(request, " - Paid!")
            f.write(f"Request of {request} paid in full.\n")
            kitty = kitty - request
        else:
            print(request, "request cannot be processed in full (Insufficient funds available). Amount paid:", kitty)
            f.write(f"Request of {request} could not be paid in full. Partial payment of {kitty} made\n")
            kitty = 0

