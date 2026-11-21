numbers = [4, 7, 2, 4, 9, 7, 4, 5, 7, 7]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

print("Number frequencies:")

for number, count in frequency.items():
    print(f"{number} found {count} times")

print("\nDuplicate numbers:")

for number, count in frequency.items():
    if count > 1:
        print(f"{number} found {count} times")
