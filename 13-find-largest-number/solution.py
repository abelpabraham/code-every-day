n = int(input("How many numbers? "))

c1 = int(input("Enter number 1: "))
check = c1

for i in range(2, n + 1):
    c1 = int(input(f"Enter number {i}: "))

    if c1 > check:
        check = c1

print(f"The largest number is {check}.")
