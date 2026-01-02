# A perfect number is a positive integer that is equal to the sum
# of its proper divisors (excluding itself).
# Example: 6 → 1 + 2 + 3 = 6

number = int(input("Enter a number: "))

i = 1
total = 0

# Check all numbers smaller than the given number
while i < number:
    # If i divides the number without remainder, it is a divisor
    if number % i == 0:
        total += i
    i += 1

# Compare the sum of divisors with the original number
if total == number:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
