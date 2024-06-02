lst = ['a', 'b', 'c', 'b', 'm', 'n', 'n']
duplicates = []

for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
        if lst[i] not in duplicates:
            duplicates.append(lst[i])

print(duplicates)

