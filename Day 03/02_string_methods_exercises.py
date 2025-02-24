secret_message = "    Programming in Python is not only powerful but also fun!  "

# Task 1
# Expected Output
# "PYTHON- POWERFUL"

# modified_message = secret_message.strip(" ")
# first_index = modified_message.find("Python")
# pyt_word = modified_message[15:21]
# pwrfl_word = modified_message[34:42]
# print((pyt_word + "-" + pwrfl_word).upper())

##DOT CHAINING
##removing unneccessary lines and putting everything on one line using "."
##chaining will change if data type changes mid-strip

# Task 2
flipped_message = "!nuf sseldnE dna seitinutropppo lufrewop htiw nohtyP"
# Expected output
# "python 🗡️ powerful🌸"
message = flipped_message[::-1]
strng1 = message[:6]
strng2 = message[12:17]
print(strng1.lower() + " 🗡️  " + strng2 + "  🌸")

# print(pyt_word.lower() + " 🗡️  " + pwrfl_word + " 🌸")

# # Task 1.3

# # After the 🔑
# message = "    🚨🔍📱🔑secret_code✌️"

# # Output
# # SECRET_CODE✌️
# ind = message.find("🔑") + 1
# print(message[ind:].upper())
