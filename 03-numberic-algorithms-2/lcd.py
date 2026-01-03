# This program calculates the Least Common Multiple (LCM)
# of two integers using the relationship between LCM and GCD.
#
# Formula:
# LCM(a, b) = |a × b| / GCD(a, b)

def gcd(a: int, b: int) -> int:
    # Euclidean Algorithm for GCD
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return abs(a * b) // gcd(a, b)


# Get input from the user
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

print("LCM:", lcm(number1, number2))
