A = int(input("Enter a number: "))

def check_odd_or_even(n):
    n1 = n // 2
    n2 = n / 2

    if n1 == n2:
        return "entered number is even"
    else:
        return "entered number is odd"

print(check_odd_or_even(A))
