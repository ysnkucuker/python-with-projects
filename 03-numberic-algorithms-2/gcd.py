# This program calculates the Greatest Common Divisor (GCD)
# of two integers using the Euclidean Algorithm.
# The Euclidean Algorithm is based on the principle that
# gcd(a, b) = gcd(b, a % b)

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# Get input from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("GCD:", gcd(number1, number2))
