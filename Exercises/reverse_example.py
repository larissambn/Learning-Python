# Print reversed name
name = input ("First and last name to reverse")

words = name.split(" ")

for word in words:
    lastindex = len(word) -1
    for index in range(lastindex, -1, -1):  # last index for the name then last index of the word
        print(word[index],end = "") # index of the world goes keeps looping until the end of the word, since it has not defined.
    print(end = "") # end of the loop
print(end ="") # print all words

# OR

Name = input ("...")

first, last = Name.split(" ") # first and last are variables part of the Name variable.

print(first[::-1], last[::-1]) # index starting from the last word until end of the string.
