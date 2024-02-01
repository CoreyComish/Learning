# Debugging Exercises from: https://education.launchcode.org/lchs/chapters/errors-and-debugging/exercises.html

# Fix the logic errors in the code to correctly report a student's letter grade!

output = "The student's score of {0}% is a(n) '{1}'."

score_percent = 79.99

if score_percent >= 90:
  letter_grade = 'A'
elif score_percent >= 80:
  letter_grade = 'B'
elif score_percent >= 70:
  letter_grade = 'C'
elif score_percent >= 60:
  letter_grade = 'D'
else:
  letter_grade = 'F'

print(output.format(score_percent, letter_grade))