#Ask the user for the two int values to compre
x = int(input("What's X? "))
y = int(input("What's Y? "))

#Now that we have the values we can compare
# We can ask less questions

if x < y:
    print("x is less than y")

# If x is less than y, print messsage no more questions
# Else

elif x > y:
    print("x is greater than y")

# If x is greater than y, print message no more questions
# Else

elif x == y:
    print("x is equal to")

# ----------- New update 1.1 -----------------------------

#Do it with even less questions
#Ask the user for the two int values to compre
x = int(input("What's X? "))
y = int(input("What's Y? "))

#Now that we have the values we can compare

if x < y:
    print("x is less than y")

# If x is less than y, print messsage no more questions
# Else if

elif x > y:
    print("x is greater than y")

# If x is greater than y, print message no more questions
# Else

#By logic when we hit this part there is no point asking or comparing

else:
    print("x is equal to y")



# ---------------- New update 1.2 ----------------------------

# If we only care about if x is equal or not we can ask less

x = int(input("What's X? "))
y = int(input("What's y? "))

# Ask less questions

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# --------------- New update 1.2.1 ---------------------------

# We can ask better to answer our question even by logic
# If we only care about if x is equal or not we can ask less

x = int(input("What's X? "))
y = int(input("What's y? "))

# Ask less questions

if x == y :
    print("x is equal to y")
else:
    print("x is not equal to y")

# This could be also be like:

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
