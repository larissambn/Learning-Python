class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generate_numbers(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Get the input from the user
n = int(input("Enter a number: "))

# Create an instance of the class
divisible_by_seven = DivisibleBySeven(n)

# Iterate through the numbers divisible by 7 and print them
for num in divisible_by_seven.generate_numbers():
    print(num)
