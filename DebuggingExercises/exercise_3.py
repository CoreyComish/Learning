# Debugging Exercises from: https://education.launchcode.org/lchs/chapters/errors-and-debugging/exercises.html

# This program should convert points earned to a percent. Find and fix the logic errors.
points_earned = 23.4
points_possible = 25

percentage = (points_earned/points_possible) * 100
print(f"The student earned {points_earned} points out of {points_possible}, or {percentage}%.")

# Here are some test cases:
# Earning 8 out of 10 possible points = 80.0%. 
# 11 of of 15 is 73.33333333333333%.
# 23.4 out of 25 93.6%.
