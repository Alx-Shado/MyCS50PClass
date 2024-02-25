# --------------------- Loops ------------------------------

# Print the sound that cats make 3 times

print("meow")
print("meow")
print("meow")

# ------------------- New update ----------------------------

# The previous code works fine, but is not easy to fix or scale

#We can use a new keyword "While" a keyword for loops
# "While let us ask again and again"

i = 3

while i != 0:
    print("meow")
    i = i - 1

x = 1

while x <= 3:
    print("meow")
    x = x + 1

y = 0

while y <3:
    print("meow")
    y += 1

# "For" can be also use for loops
# "List" is a new type like int strin bool

for i in [0, 1, 2]:
    print("meow")

#better yet

for _ in range(3):
    print("meow")

# ------------------- New -----------------------------------
print("meow/n" * 3, end="")

