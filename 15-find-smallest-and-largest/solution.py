
n = int(input("How many numbers? "))

if n > 0:
    number = int(input("Enter number 1: "))
    smallest = number
    largest = number

    for i in range(2, n + 1):
        number = int(input(f"Enter number {i}: "))

        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    print(f"Largest number: {largest}")
    print(f"Smallest number: {smallest}")
else:
    print("Enter a positive number.")
