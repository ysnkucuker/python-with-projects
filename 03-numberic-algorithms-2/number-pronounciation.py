# This program converts a two-digit number into its
# English pronunciation.
# Handles special cases for numbers between 11 and 19.
# Example: 12 → twelve, 42 → forty two

def number_to_words(number: int) -> str:
    ones = [
        "", "one", "two", "three", "four",
        "five", "six", "seven", "eight", "nine"
    ]

    tens = [
        "", "ten", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    # Validate input: only two-digit numbers are allowed
    if number < 10 or number > 99:
        return "Please enter a two-digit number."

    # Special case: 10–19
    if 10 <= number <= 19:
        return teens[number - 10]

    ten_digit = number // 10
    one_digit = number % 10

    return tens[ten_digit] + " " + ones[one_digit]


# Get input from the user
number = int(input("Enter a two-digit number: "))
print(number_to_words(number))
