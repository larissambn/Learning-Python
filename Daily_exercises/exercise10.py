# 10
# not completelly correct as it prints a list 

words = input("Write a sequence of whitespace separated words : ")

splitted_words = words.split() # get the string to be separated into words, not letters

unique_items = []

for item in splitted_words:
    if item not in unique_items:
        unique_items.append(item) # loop to take items from a list to another

unique_items.sort() 

print(unique_items)

# other solutions (Better)

word = input("Enter a sequence of words: ").split()
[word.remove(i) for i in word if word.count(i) > 1 ]   # removal operation with comprehension method
word.sort()
print(" ".join(word))

# other 

word = input("Write a sequence of words : ").split()

for i in word:
    if word.count(i) > 1:    #count function returns total repeatation of an element that is send as argument
        word.remove(i)     # removes exactly one element per call

word.sort()
print(" ".join(word))