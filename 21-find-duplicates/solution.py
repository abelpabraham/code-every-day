n = int(input("How many numbers: "))

if n > 0:
    duplicates = []
    numbers = []

    for i in range(1, n + 1):
        inp = int(input(f"Enter number {i}: "))

        if inp in numbers and inp not in duplicates:
            duplicates.append(inp)
        else:
            numbers.append(inp)

    if len(duplicates) > 0:
        print("Duplicate numbers:")
        for number in duplicates:
            print(number)
    else:
        print("There are no duplicates!")
else:
    print("Enter a positive number.")
