# Debugging Exercises from: https://education.launchcode.org/lchs/chapters/errors-and-debugging/exercises.html

import string
alphabet = string.ascii_uppercase
# The code below contains 3 syntax errors. Run the code as-is to generate the first error message.
# Use the message to find and fix the bug. Repeat for the other bugs.

value = int(input("Enter an index value: "))
index = value % 26

if value >= len(alphabet):
  print("The letter at index {0} ({1}) is '{2}'.".format(value, index, alphabet[index]))
else:
  print("The letter at index {0} is '{1}'".format(index, alphabet[index]))