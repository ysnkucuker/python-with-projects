print("""
Factorial Calculator

Press 'q' to quit the program.
""")

def calculate_factorial(number: int) -> int:
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    return factorial


while True:
    user_input = input("Enter a number: ")

    if user_input.lower() == 'q':
        print("Program terminated.")
        break

    if not user_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    number = int(user_input)

    result = calculate_factorial(number)
    print(f"Factorial of {number} is: {result}")
