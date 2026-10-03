N = int(input("Enter a positive integer: "))

Total = 0

for i in range(1, N + 1, 2):
    Total = Total + 1

print(f"No. of odd numbers from 1 - {N} is {Total}")
