no_of_inputs = int(input("How many numbers: "))

if no_of_inputs > 0:
    sum_of_numbers = 0

    for i in range(1, no_of_inputs + 1):
        number = int(input(f"Enter number {i}: "))
        sum_of_numbers += number

    average_of_inputs = sum_of_numbers / no_of_inputs

    print(f"Average of entered numbers = {average_of_inputs}")
else:
    print("Enter a positive number.")
