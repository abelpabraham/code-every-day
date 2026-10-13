n = int(input("How many numbers? "))

if n > 0:
    n1 = int(input("Enter number 1: "))
    smallest = n1

    for i in range(2, n + 1):
        n1 = int(input(f"Enter number {i}: "))

        if n1 < smallest:
            smallest = n1

    print(f"The smallest number is {smallest}.")
else:
    print("Enter a positive number.")
