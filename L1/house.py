# Match is like switch on other coding lenguages

name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# --------------------- New -------------------------------

# Ask user for name

name = input("What's your name? ")

if name == "Harry" or name == "Herminone" or name == "Ron":
    print(f"Hello {name} from Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# --------------------- New -------------------------------

name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# --------------------- New -----------------------------------

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")