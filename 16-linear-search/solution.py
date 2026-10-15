
number_count = int(input("How many numbers? "))

if number_count > 0:
    found = False

    target = int(input("Enter number to search for: "))

    for i in range(1, number_count + 1):
        number = int(input(f"Enter number {i}: "))

        if number == target:
            found = True

    if found:
        print("Number found!")
    else:
        print("Number not found!")
else:
    print("Enter a positive number.")
