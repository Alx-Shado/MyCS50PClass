# docs.python.org/3/libary/stdtypes.html#string-methods

#Ask the user for their name
name = input("What's your name?")

#Remove whitespace from str and capitalize user's name
name = name.strip().title()

print(f"Hello, {name}")

# OR

# Compact Code
name = input ("What's your name").strip().title()