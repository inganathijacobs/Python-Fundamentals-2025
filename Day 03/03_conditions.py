# Conditions( Control flow)
# Take a decision ➡️ Choice

# If .. else
# If it is <= 2 = bike, Else =car
no_of_person = 10

##Condition souuld return boolean| if expects a boolean
if no_of_person <= 2:
    print("We will take the bike for the party")
else:
    print("We will take the car for the party")


# Task
# Get two person name
# Case 1
# Ethan, Luvuyo
# 185cm, 175cm
# print whoever is taller
# Ethan is taller than Luvuyo by 10cm

# Case 2
# Ethan, Luvuyo
# 185cm, 194cm
# print whoever is taller
# Luvuyo is taller than Luvuyo by 9cm

name1 = input("Please enter your name: ")
height1 = abs(float(input("Please enter your height: ")))
name2 = input("Please enter your name: ")
height2 = float(input("Please enter your height: "))
difference1 = height1 - height2
difference2 = height2 - height1
if height1 > height2:
    print(f"{name1} is taller than {name2} by {difference1}cm")
elif height1 == height2:
    print(f"{name1} and {name2} are of the same height")

else:
    print(f"{name2} is taller than {name1} by {difference2}cm")


# Task 1.2
# Case 3:
# Ethan, Luvuyo
# 185cm, 185cm
# Ethan and Luvuyo are of the same height
# Clue: elif

# Task 1.3
# Improve code quality
# Clue: abs()
name1 = input("Please enter your name: ")
height1 = abs(float(input("Please enter your height: ")))
name2 = input("Please enter your name: ")
height2 = float(input("Please enter your height: "))

difference2 = abs(height2 - height1)
if height1 > height2:
    print(f"{name1} is taller than {name2} by {difference2}cm")
elif height1 == height2:
    print(f"{name1} and {name2} are of the same height")

else:
    print(f"{name2} is taller than {name1} by {difference2}cm")
