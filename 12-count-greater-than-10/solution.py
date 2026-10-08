n = int(input("Enter a positive integer: "))

count = 0

if n <= 10:
    print("There are no numbers greater than 10.")
else:
    for i in range(11, n + 1):
        count += 1

print(f"There are {count} numbers that are greater than 10.")
