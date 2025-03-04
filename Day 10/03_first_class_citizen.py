## In Python
# Function treated first class citizen(value)


# Rules
# 1. Assign to variable
# 2. Pass as argument
# 3. Return


# Rules
# 1. Function :Assign to variable
# 2. Function:Pass as argument
# 3. Function:Return

# 1. Assign to variable
# x = 1


# def greet(name):
#     return f"Hi,{name}"


# print(type(greet))  # <class 'function'>
# # 1. Assign variable
# y = greet  # function
# print(y("Jamie"))


# 2.Function : Pass as argument: say_hello (function) is passed as argument


# def say_hello():
#     return "Hello, "


# def greeting(hello_msg, name):
#     print(hello_msg() + name)


# greeting(say_hello, "Python!")  ## Function id getting passes as argument

##Functional languages
# - F#
# - Haskell (no loops->recursion(function calling itself)) || Facebook comments uses it for filtering bad comments
# - Scala


# 3. Function : Returned


def f1():
    def f2():
        return "Hi😆👋"

    return f2


print(f1()())  ## first returns f2, then after returns the return of f2
