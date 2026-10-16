n = int(input("Enter how many numbers? "))
target = int(input("Enter the target number: "))
t_count = 0

for i in range(1, n + 1):
    number = int(input(f"Enter number {i}: "))

    if target == number:
        t_count += 1

print(f"Number of occurrences of {target}: {t_count}")

if t_count == 0:
    print(f"{target} is not present!")
