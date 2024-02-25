#Ask user imput, and convert string to float for decimals

x = float(input("What's X? "))
y = float(input("What's Y? "))

print (x + y)

#Ask user imput, and convert string to float, and round the result
# docs.python.org/3/libary/funtions.html#round

X = float(input("What's X? "))
y = float(input("What's Y? "))

#Print round result
#round(number[, ndigits])

z = round(x + y)
print (z)

#OR

print(round(x + y))

#format in python

x = float(input("What's X? "))
y = float(input("What's Y? "))

z = round (x + y)

print (f"{z:,}")