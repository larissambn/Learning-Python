user_input = input("Write a sentence of words or numbers :")  
stgs = user_input.split()

stg_counts = {}

for stg in stgs:
    if stg in stg_counts:
        stg_counts[stg] += 1
    else:
        stg_counts[stg] = 1

# Sort the dictionary by keys alphanumerically
sorted_dict = dict(sorted(stg_counts.items()))

# Print the sorted dictionary
for key, value in sorted_dict.items():
    print(key, ":", value)
