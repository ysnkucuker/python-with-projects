# This program finds all proper divisors of a given number.
# Proper divisors are numbers that divide the given number
# without remainder, excluding 1 and the number itself.
# Example: 12 → 2, 3, 4, 6

def get_divisors(number: int) -> list:
    divisors = []

    # Check all numbers from 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)

    return divisors


while True:
    user_input = input("Enter a number (press 'q' to quit): ")

    if user_input.lower() == "q":
        print("Program terminated.")
        break

    if not user_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    number = int(user_input)
    print("Divisors:", get_divisors(number))
