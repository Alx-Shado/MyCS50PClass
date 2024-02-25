# docs.python.org/3/libary/stdtypes.html#string-methods

#Ask the user for their name
name = input("What's your name?")

#Remove whitespace from str and capitalize user's name
name = name.strip().title()

#Split username into first name and last name

first, last = name.split(" ")

print(f"Hello, {first}")
