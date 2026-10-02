N = int(input("Enter a number: "))

total = 0

for i in range(1, N + 1):
    M = i % 2

    if M == 0:
        total = total + 1

print(f"No. of even numbers from 1 - {N} is {total}")
