words = input("Write a sequence of whitespace separated words: ")
splitted_words = words.split()

unique_items = []

for item in splitted_words:
    if item not in unique_items:
        unique_items.append(item)

unique_items.sort()

print(unique_items)



