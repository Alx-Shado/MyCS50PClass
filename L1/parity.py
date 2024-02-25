# ------------------- How "%" Works ------------------------

# It is used for cases in we have a remainder on a division

# How we determine is "n" number is even or odd?
# Even number can be divided by 2 with no remainder

#Ask user for the int

# x = int(input("What's X? "))

# if x % 2 == 0:
#    print("Even")
# else:
#    print("Odd")

# --------------- New update --------------------------------

#What can we do better?

#we can creat a function to solve the same issue
    
def main():
    x = int(input("What's X? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

#We can return only what we care, as True or False
# bool can only be True or False

# ---------------- New Pythonic Update ------------------------

# Features that only Python have

def is_even(n):
    return True if n % 2 ==0 else False

# Features we can return only the answer with out having to
# Ask again in the def

def is_even(n):
    return n % 2 == 0