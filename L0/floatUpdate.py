# Ask user input, convert string to float
x = float(input("What's X? "))
y = float(input("What's Y? "))

z = x / y

print (z)

# Update round the division result
z = round(x / y, 2)

print ("Float Result with only two", z)

z = x / y

print("Float Result wih format" f"{z:.2f}")