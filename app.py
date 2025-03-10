# Get user input
user_number = int(input("Enter a number to convert into words! 🔢➡️🔡 : "))

# List for numbers 0 to 19
ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

# List for tens like 20, 30, 40, etc.
tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

# Logic for converting numbers to words
def number_to_words(num):
    if num == 0:
        return 'Zero'

    word = ''

    # Handle thousands (1000-9999)
    if num // 1000 > 0:
        word += ones[num // 1000] + " Thousand "
        num %= 1000

    # Handle hundreds (100-999)
    if num // 100 > 0:
        word += ones[num // 100] + " Hundred "
        num %= 100

    # Handle tens and ones (0-99)
    if num > 0:
        if num < 20:  # For numbers 1-19
            word += ones[num]
        else:  # For numbers 20 and above
            word += tens[num // 10]
            if num % 10 > 0:
                word += "-" + ones[num % 10]

    return word.strip()

# Print the result
print(number_to_words(user_number))

          
    