# def greet(name):
#     return f"Hi,{name}"


# # Lamba expression: Function one liner

# greet1 = (
#     lambda name: f"Hi,{name}"
# )  ## Keep lambda without name but it is useless because you need to name it to use it.
# ## implicit return on right -hand side

# print(greet1("Jevan"))
# print(greet("Jevan"))
greet = lambda name: f"Hi {name}"
print(greet("Inga"))

# # Summary:
# # 1. Anonymous -nameless function
# # 2. One liner
# # 3. Implicit return (automatically)


# def add(n1, n2):
#     return n1 + n2


# add1 = lambda n1, n2: n1 + n2
# print(add1(9, 8))
# print(add(9, 8))


# # Map and Filter
# player_stats = [10, 30, 60]
# boosted_stats = map(
#     lambda x: x * 2, player_stats
# )  ##takes in function and iterable(list,dictionary,tuple)
# print(boosted_stats, list(boosted_stats))  ##change it to list

# boosted_stats1 = map(
#     lambda x: x * 2,
#     [10, 30, 60],  # list of int
# )  ## each element is the lambda functions argument
# print(list(boosted_stats1))


# ##MAP AND FILTER is a higher order function-> takes another function as argument (HOF)
# ##Map works for both normal functon and for Lambda function


# # Lambda vs def
# # - choose def if you will need to reuse the code elsewhere
# # - choose lambda if it is one time use and because it is concise


result = filter(
    lambda x: x > 10, [10, 30, 60]
)  ## if result is true then it will be added to output
print(result, list(result))

# gt1 = lambda x: x > 10  ## Returns true or false|| gt1 => predicate-> returns boolean
# result = filter(gt1, [10, 30, 60])

# Map
# 1. len(input _list)== len(output_list)
# 2. Transform data type
# 3. Returns copy of list (original list won't be affected)


# Filter
# 1. len(input_list)>= len (output_list)
# 2. You cannot change data type | Input data type and output data type will be the same
# 3. Doesn't affect the original list/ input list | Output is a copy

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
# Task 1.1
# Task (map or filter)
# Number letter in the name
# [4, 8, 11, 15, 10, 4]


letters = map(lambda name: len(name), avengers)
print(list(letters))


# letters = map(lambda x: len(x), avengers)
# print(list(letters))


# Task 1.2

# Find longer names more the 10 letters name and stored in a new list

# Output
# ["Black widow", "Captain america"]
longer_words = filter(lambda x: len(x) > 10, avengers)
print(list(longer_words))


# Task 1.3

# Find the passed student's names (pass criteria >= 40)

# Output
# ["Lillian Ellis", "Debra Beard",  "Nettie Hancock" ]
scores = [
    {
        "marks": 32,
        "name": "Yvette Merritt",
    },
    {
        "marks": 57,
        "name": "Lillian Ellis",
    },
    {
        "marks": 22,
        "name": "Mccall Carter",
    },
    {
        "marks": 21,
        "name": "Pate Collier",
    },
    {
        "marks": 91,
        "name": "Debra Beard",
    },
    {
        "marks": 75,
        "name": "Nettie Hancock",
    },
    {
        "marks": 20,
        "name": "Hatfield Hodge",
    },
]


passed_students = filter(lambda student: student["marks"] >= 40, scores)
names = map(lambda student: student["name"], passed_students)
print(list(names))


# students = filter(lambda student: student["marks"] >= 40, scores)
# name = map(lambda student: student["name"], students)
# print(list(name))


# ## Task 1.4
# Find the topper

# Clue:
# Use sorted()

# Output
# Debra Beard

studs = sorted(scores, key=lambda student: student["marks"])
top = studs[-1]


# sorted_students = sorted(scores, key=lambda student: student["marks"])
# topper = sorted_students[-1]
# print(topper["name"])
