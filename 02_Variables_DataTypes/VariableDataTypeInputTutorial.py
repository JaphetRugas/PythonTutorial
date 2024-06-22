# -----------------------------------------------------------
# Data Types Section
# -----------------------------------------------------------
# This section introduces basic data types in Python.
# We explore strings, integers, floats, and booleans with examples.
# Each example is commented out for reference.

# Examples of data types:
# firstName = "Jade Japhet"   # string: Represents a sequence of characters.
# lastName = "Rugas"          # string: Represents another sequence of characters.
# age = 23                    # int: Represents an integer number.
# money = 10.10               # float: Represents a floating-point number.
# isMale = True               # boolean: Represents a Boolean value (True or False).

# Printing the variables:
# print(firstName + " " + lastName)  # Outputs the full name.
# print(age)                         # Outputs the age.
# print(money)                       # Outputs the monetary amount.
# print(isMale)                      # Outputs the Boolean value.

# -----------------------------------------------------------
# User Input Section
# -----------------------------------------------------------
# This section demonstrates how to use input to get user data.
# We ask the user for their first name and print it back to them.

# Asking for user input:
# firstName = input("Enter your first name: ")  # Captures user input as a string.

# Printing the user's first name:
# print(firstName)

# -----------------------------------------------------------
# Casting Variables
# -----------------------------------------------------------
# This section covers how to cast (convert) variables from one type to another.
# For example, converting a number to a string or a string to a float.

# Casting examples:
# str(number)  # Converts a number to a string.
# int(string)  # Converts a string to an integer.
# float(string)  # Converts a string to a float.

# Demonstrating casting:
# firstName = "Jade"      # A string variable.
# number = 5              # An integer variable.
# money = "5.25"          # A string that represents a float value.

# Printing combined variables:
# print(firstName + str(number))  # Concatenates string with a number (as a string).
# print(number + float(money))    # Adds an integer to a float (converted from a string).

# -----------------------------------------------------------
# Arithmetic Operations
# -----------------------------------------------------------
# This section covers basic arithmetic operations like addition, subtraction, multiplication, and division.
# We demonstrate how to perform these operations with different types of data.

# Example arithmetic operations:

# Subtraction
print(5 - 2)  # Outputs: 3

# Addition
print(5 + 2)  # Outputs: 7

# Multiplication
print(5 * 2)  # Outputs: 10

# Division
print(5 / 2)  # Outputs: 2.5

# Floor Division (integer division)
print(5 // 2)  # Outputs: 2

# Modulus (remainder)
print(5 % 2)  # Outputs: 1

# Exponent (power)
print(5 ** 2)  # Outputs: 25

# -----------------------------------------------------------
# One Function Calculator - Simple Version
# -----------------------------------------------------------
# This section shows a simple calculator that performs subtraction.
# It takes two numbers from the user and calculates their difference.

# Getting the first number from the user:
firstNumber = int(input("First Number: "))  # Converts input to integer.

# Getting the second number from the user:
secondNumber = int(input("Second Number: "))  # Converts input to integer.

# Calculating the result of subtraction:
result = str(firstNumber - secondNumber)  # Converts result to string for printing.

# Printing the result in a readable format:
print(str(firstNumber) + " - " + str(secondNumber) + " = " + result)  # Outputs the formatted result.
