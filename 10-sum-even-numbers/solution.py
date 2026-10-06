n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print(f"Sum of even numbers between 1 and {n} is: {total}")
