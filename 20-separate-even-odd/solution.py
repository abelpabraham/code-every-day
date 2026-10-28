n = int(input("How many numbers? "))

odd = []
even = []

if n > 0:
    for i in range(1, n + 1):
        number = int(input(f"Enter number {i}: "))

        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    print("Odd numbers:")
    for number in odd:
        print(number)

    print("Even numbers:")
    for number in even:
        print(number)
else:
    print("Enter a positive number.")
