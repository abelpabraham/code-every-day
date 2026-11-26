numbers = [4, 7, 2, 4, 9, 7, 4, 5, 7, 7, 9, 9, 9]

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

most_frequent = 0
highest_frequency = 0

second_most_frequent = 0
second_highest_frequency = 0

for number, count in frequency.items():
    if count > highest_frequency:
        second_most_frequent = most_frequent
        second_highest_frequency = highest_frequency

        most_frequent = number
        highest_frequency = count

    elif count > second_highest_frequency:
        second_most_frequent = number
        second_highest_frequency = count

print(f"Second most frequent number: {second_most_frequent}")
print(f"Frequency: {second_highest_frequency}")
