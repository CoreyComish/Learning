# Debugging Exercises from: https://education.launchcode.org/lchs/chapters/errors-and-debugging/exercises.html

word = input("Enter a school-appropriate word: ")
print("The last letter in '{0}' is '{1}'".format(word, word[len(word)-1]))

first_num = int(input("Enter a whole number: "))
second_num = int(input("Enter another whole number: "))

print(f"For {first_num} and {second_num}:")
print("\tSum = {0}".format(first_num + second_num))
print("\tDifference = {0}".format(first_num - second_num))
print("\tProduct = {0}".format(first_num * second_num))
if second_num != 0:
  print("\tQuotient = {0}".format(first_num / second_num))
else:
  print("\tQuotient = undefined (cannot divide by 0)")