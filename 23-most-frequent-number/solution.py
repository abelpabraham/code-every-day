numbers = [4, 7, 2, 4, 9, 7, 4, 5, 7, 7]

frequency = {}

for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

most_frequent = 0
number_of_frequencies = 0

for number, count in frequency.items():
    if count > number_of_frequencies:
        most_frequent = number
        number_of_frequencies = count

print(
    f"Most frequent number is {most_frequent} "
    f"and it was shown for {number_of_frequencies} times."
)
