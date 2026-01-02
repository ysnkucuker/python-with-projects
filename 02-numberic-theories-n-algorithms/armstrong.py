# An Armstrong number is a number that is equal to the sum of its digits
# each raised to the power of the number of digits.
# Example: 153 → 1³ + 5³ + 3³ = 153

number_str = input("Enter a number: ")
digit_count = len(number_str)
number = int(number_str)

total = 0
temp = number

# Process each digit of the number
while temp > 0:
    digit = temp % 10
    total += digit ** digit_count
    temp //= 10

# Check if the calculated sum equals the original number
if total == number:
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")
