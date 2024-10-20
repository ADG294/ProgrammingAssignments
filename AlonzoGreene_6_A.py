import re

# This program imports the regular expression package then

# creates functions that validate different patterns.

# The program then asks a user for input then calls the previous

# created functions on the input.

# Create a function to validate phone numbers.

def valid_phone(n):

    # Create a regular expression pattern for phone numbers.

    pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

    # Create an if/else statement that validates if the input is a full match

    # to the pattern.

    if re.fullmatch(pattern, n):
        print("valid phone number.")
    else:
        print("invalid phone number.")


# Create a function to validate social security numbers.

def valid_ssn(ssn):

    # Create a regular expression pattern for a social security number.

    pattern = r'\d\d\d-\d\d-\d\d\d\d'

    # Create an if/else statement that validates if the input is a full match

    # to the pattern.

    if re.fullmatch(pattern, ssn):

        print("valid ssn number.")

    else:

        print("invalid ssn number.")


# Create a function to validate zip codes.

def valid_zip(zip_c):

    # Create a regular expression pattern for zip codes.

    pattern = r'\d\d\d\d\d'

    # Create an if/else statement that validates if the input is a full match

    # to the pattern.

    if re.fullmatch(pattern, zip_c):

        print("valid zip code.")

    else:

        print('invalid zip code.')


# Create the main function.

def main():

    # Ask user for input

    n = input('Enter your phone number: \n')

    # Call the phone number validation function.

    valid_phone(n)

    # Ask user for input

    ssn = input('Enter your ssn: \n')

    # Call the social security number validation function.

    valid_ssn(ssn)

    # Ask user for input

    zip_c = input('Enter your zip code: \n')

    # Call the zip code validation function.

    valid_zip(zip_c)

# Call main function to execute program.

main()


