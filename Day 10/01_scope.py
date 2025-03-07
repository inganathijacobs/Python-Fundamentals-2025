## Scope of variable
## Lifetime of variable
## Domain/AREA in which the variable is alive/exists

t1 = 100


def simple():
    t2 = 10


simple()
## print(t1, t2) | t2 scope is within the function only and it cannot be accessed outside the function
# t2 is in the simple() function scope

price = 100  ## It is in a lexical scope


## Case 1 : MIGHT BE QUESTION  IN TEST!!!!!!
def get_price():
    print("The price of the books is: ", price)


get_price()
## get_price
# 1. First checks for local 'price' variable
# 2. Then goes to outer scoper (lexical scope)


##Closure
# own scope + lexical scope

# Case 2:


code_word = "Hulk"


def space_ship():
    question = "Please provide code word"

    def code_word_check():
        password = "Hulk"
        print(question)

        if password == code_word:
            print(f"Welcome, {password} the strongest avenger 💪")
        else:
            print("❌ Access denied to 🚀")

    code_word_check()


space_ship()


# Assignment:
# Write a comparison in terms of scope on keywords
# global vs nonlocal
# with examples
