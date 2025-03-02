fav_movie = "John Wick"

# get only 'J'

# Index
print(fav_movie[0])
print(fav_movie[5])

# Negative index
print(fav_movie[-1])
print(fav_movie[-2])

# Only Wick
print(fav_movie[5] + fav_movie[6] + fav_movie[7] + fav_movie[8])
print(fav_movie[-4:])

# Slice operator (:)
# fav_movie[start:end]- end index not included, step +1
print(fav_movie[2:9])

# another method without specifying end
print(fav_movie[2:])

# used for when you want to copy a string
print(fav_movie[:])

print(fav_movie[5:9])
print(fav_movie[5:])
print(fav_movie[-4:])

##step +1 (jumping by 1)
print(fav_movie[2:9])

# jumping twice
print(fav_movie[2:9:2])

##reversing string, step<0, will start from end value and keep substracting 1
print(fav_movie[::-1])  # kciW nhoJ


print(fav_movie[-4::-1])  # W nhoJ

# will get blank value because it is impossible
print(fav_movie[-4:-1:-1])

# immutable- cannot modify value in Python
# fav_hero[0] = 't' ❌


fav_hero = "The Hulk"
changed_letter = fav_hero[:4] + "h" + fav_hero[5:9]
print(changed_letter)
print(fav_hero[:4] + "h" + fav_hero[-3:])


catchphrase = "I am Groot"

print(catchphrase.upper())  ##makes every letter capital
print(catchphrase.lower())  ##makes every letter lower
print(catchphrase.capitalize())  ## capitalises only the first letter of entire string
print(catchphrase.title())  ## makes every first letter of word capital
print(catchphrase.swapcase())

##remove spaces or symbols
message = "     With greater power comes great responsibility   "
clean_message = message.strip()
print(clean_message)

##immutable so it won't change
print(message)

##strip only removes leading and trailing characters and not in between letters
coded_message = "****SO*S******"
decoded = coded_message.strip("*")
print(decoded)
##SO*S

##lstrip() removes left part
##rstrip() removes the right part

quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.count("Dream"))

##replace
dream = "🛌💭"
str = quote.replace("Dream", dream)
print(str)

print(quote.replace("Dream", "🛌💭", 1))


##finds the first index of the first occurence of the word/string, if string is not there then it returns -1
print(quote.find("something"))
print(quote.find("**"))
