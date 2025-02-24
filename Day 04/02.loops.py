# print("Vote for Jevan")
# print("Vote for Jevan")
# print("Vote for Jevan")


# # Refactor in 'while' loop
# i = 1

# while i <= 3:
#     print("Vote for Jevan")
#     i = i + 1


# # Refactor in 'for' loop
# # for and range come in (pair)

# for i in range(3):
#     print(i)

# # Task 1: # Print only odd numbers from 1 to 50 (HARD)
# for i in range(1, 51):
#     #     if i % 2 != 0:
#     print(i)
# # Task 1(EASIER)
# for i in range(1, 50, 2):
#     print(i)
# # Task (MY APPROACH)

# for i in range(1, 51):
#     if i % 2 != 0:
#         print(i)

# for i in range(1, 4):
#     print("Vote for Jevan")

# PRINT PATTEN
# Task 1.1
# While loop
# 🔥
# 🔥🔥
# 🔥🔥🔥
# 🔥🔥🔥🔥
# 🔥🔥🔥🔥🔥
# REPETITION OPERATOR(*)
i = 1
# emoji = "🔥"
# while i <= 5:
#     print(emoji * i)  # repeat fire by i times
#     i = i + 1


# Task 1.2
# Refactoring with for Loop
# 🔥
# 🔥🔥
# 🔥🔥🔥
# 🔥🔥🔥🔥
# 🔥🔥🔥🔥🔥
# for i in range(1, 6, 1):
#     print(emoji * i)
# i = i + 1


# Task 1.3 (with while loop)
# Output
# Please tell the no of rows?: 3
# Please tell the pattern?:
# 🍧
# 🍧
##🍧🍧
# 🍧🍧🍧
# rows = int(input("Please tell the no of rows: "))
# emoji1 = input("Please tell the emoji: ")
# while i <= rows:
#     print(emoji1 * i)
#     i = i + 1

# Task 1.4 (Refactor with for loop)
# Clue: range has 3 arguments
# Output
# Please tell the no of rows?: 3
# Please tell the pattern?:
# 🍧
# 🍧
# 🍧🍧
# 🍧🍧🍧
rows = int(input("Please tell the no of rows: "))
emoji1 = input("Please tell the emoji: ")
for i in range(rows + 1):
    print(emoji1 * i)
