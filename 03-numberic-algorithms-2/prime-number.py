# A prime number is a natural number greater than 1
# that has no positive divisors other than 1 and itself.
# Examples: 2, 3, 5, 7, 11

def is_prime(number: int) -> bool:
    # 1 is not a prime number
    if number <= 1:
        return False

    # 2 is the smallest and only even prime number
    if number == 2:
        return True

    # Check divisibility from 2 to number - 1
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


while True:
    user_input = input("Enter a number (press 'q' to quit): ")

    if user_input.lower() == "q":
        print("Program terminated.")
        break

    if not user_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    number = int(user_input)

    if is_prime(number):
        print("The number is prime.")
    else:
        print("The number is not prime.")
