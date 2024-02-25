#Update the parameters on the funcion

def hello(to):
    print("Hello,", to)

# Same as:
#def hello(x):
#    print("Hello,", x)

name = input("What's your name? ")

# Calling the funtion and passing the name argument as input variable
hello(name)

#2nd Update, setting a defult value on our funtion

def hello(to="World"):
    print("hello,", to)

#Calling our funtion with input to print our defult value
hello()

#Asking user for name

name = input("What's your name? ")

#Calling our funtion and pass the argument "name" as value

hello(name)
