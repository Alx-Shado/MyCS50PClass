# We now discuss a new keyword "and"
# "and" is a conjuntion of two of more questions

# Let's consider what grade a studen should get.
# The grade depends on the score range

# First we need to get the score:

score = int(input("Score:"))

# Now that we have the score
# How do we assing the grade base on the range?

#This will be a good start:

if score >= 90 and score <= 100:
    print("Student Grade: A")
elif score >= 80 and score <= 89:
    print("Student Grade: B")
elif score >= 70 and score <= 79:
    print("Student Grade: C")
elif score >= 60 and score < 70:
    print("Student Grade: D")
else:
    print("Studen Grade: F")

# We can then switch things up
    
if 90 <= score and score <= 100:
    print("Student Grade: A")
elif 80 <= score and score <= 90:
    print("Student Grade: B")
elif 70 <= score and score <= 80:
    print("Student Grade: C")
elif 60 <= score and score <=70:
    print("Student Grade: D")
else:
    print("Grade: F")

# Now python can let us do even better

if 90 <= score <= 100:
    print("Student Grade A")
elif 80 <= score < 90:
    print("Student Grade: B")
elif 70 <= score < 80:
    print("Student Grade: C")
elif 60 <= score <70:
    print("Student Grade: D")
else:
    print("Grade: F")

# ------------------- New Update ----------------------------

score = int(input("Score: "))

# If we change the way we think about the issue
# we supose that the score numer will be always from 0 to 100
# We can make some assumtions

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#The previous code ask less questions in each case.