# # Task 1
# degrees = input("Please provide your Fahrenheit: ")
# amount = 5 / 9 * (float(degrees) - 32)
# print(f"The {degrees}°F is {amount}°C")

# # Task 2
# birth_Year = input("Please provide your birth year: ")
# age = 2025 - int(birth_Year)
# print(f"Your age is {age}")

# Task 3
PI = 3.14
radius = input("Provide the radius of the cirle: ")
area = PI * (float(radius) ** 2)
print("Area of circle is: " + str(area))

# Task 4
get_Input = input("Input: ")
loader = int(get_Input) // 10
loader_Display = loader * "="
space = (10 - int(loader)) * " "
print("[" + loader_Display + str(space) + "]")
