def average(s, l):
    return s / l


no_of_numbers = int(input("How many numbers? "))

if no_of_numbers > 0:
    numbers = []

    for i in range(1, no_of_numbers + 1):
        num = int(input(f"Enter number {i}: "))
        numbers.append(num)

    average_of_numbers = average(sum(numbers), len(numbers))

    larger_than_average = []

    for num in numbers:
        if num > average_of_numbers:
            larger_than_average.append(num)

    print(f"Average of numbers = {average_of_numbers}")
    print(
        f"There are {len(larger_than_average)} "
        "numbers larger than average."
    )

    for num in larger_than_average:
        print(num)
else:
    print("Enter a positive number.")
