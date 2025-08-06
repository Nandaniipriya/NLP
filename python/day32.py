# Python Question: Finding the largest number that can be divided by each digit in a number without any remainder

'''
Suppose you have a number and you want to find the largest number that can be obtained by multiplying its digits without any remainder. For example, consider the number 123.

Input: A number (123)
Output: 6 (The largest number obtained by multiplying 123's digits: 1 x 2 x 3 = 6)

Input: Another number (456)
Output: 120 (The largest number obtained by multiplying 456's digits: 4 x 5 x 6 = 120)
'''

# Solution
def find_largest_digit_product(number):
    # Check if the number is less than 10
    if number < 10:
        return number

    # Find the digits of the number
    digits = str(number)

    # Initialize the largest digit product as 1
    largest_digit_product = 1

    # Loop through each digit and calculate its product
    for digit in digits:
        # Calculate the product of the current digit
        current_digit_product = int(digit) * find_largest_digit_product(int(digit))

        # Update the largest digit product if the current digit product is greater
        largest_digit_product = max(largest_digit_product, current_digit_product)

    return largest_digit_product

# Test cases
number = 123
print("Largest digit product for", number, "is", find_largest_digit_product(number))
number = 456
print("Largest digit product for", number, "is", find_largest_digit_product(number))