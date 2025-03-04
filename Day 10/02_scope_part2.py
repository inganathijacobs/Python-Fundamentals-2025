# # Case 2
# price = 200  ## won't exists because local variable is given preferrence


# def get_price():
#     print(
#         "The old price of the books is: ", price
#     )  ## get error ##name is noted , not value | UnboundLocalError
#     price = 100  ## will try and access this variable because it exists locally
#     print("The new price of the books is: ", price)


# get_price()
##2 Phase Execution
##1. Compilation- Declaration noted
##2. Execution - print that value

# Case 3 : Both variable name (Outside and Inside)
price = 200  # Live under the shadow
##Local scope is given higher priority


# def get_price():
#     price = 100  ##Shadowing #Legend  ##name is noted, not value, in execution, the value gets assigned to 100
#     print(
#         "The old price of the books is: ", price
#     )  # gets printed because we know price value
#     print(
#         "The new price of the books is: ", price
#     )  # gets printed because we know price value


# get_price()


## Case 4:
# Live under the shadow
##Local scope is given higher priority


# def get_price():
#     print(
#         "The old price of the books is: ", price
#     )  ##UnboundLocalError: Trying to access it before declaration
#     price = 100
#     print("The new price of the books is: ", price)


# get_price()


# Summary
# 1. Local gets preference
# 2. UnboundLocalError-> If you try access before declaration
# 3. Only functions create new scope
