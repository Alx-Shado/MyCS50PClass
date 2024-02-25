#Defining main funtion

def main():
    name = input("What's your name? ")
    hello(name)

#Defining our hello funtion

def hello(to="Wolrd"):
    print("Hello,", to)

#Callin our Main funtion, that will run the code in main callin the other funtions
main ()