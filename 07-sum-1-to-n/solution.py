a = int(input("Enter a positive integer: "))

if a > 0:
    total = 0

    for i in range(1, a + 1):
        total = total + i

    print(f"Sum = {total}")
else:
    print("Enter a positive integer greater than 0")
