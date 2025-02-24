name = "Chleo"
age = 20
balance = 1000000.50
is_Rich = True

print(name)
print(balance)
print(age)
print(is_Rich)


print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(balance))  # <class 'float'>
print(type(is_Rich))  # <class 'bool'>

print("My name is " + name)

# convert from int to string
print("My age is " + str(age))

# fstring
# {} = interpolation (substitution)
print(f"My age is {age}")
print(f"She has {2 * 1000} followers🎉")
