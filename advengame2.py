def start_adventure():
    print("Welcome to Jeremy's adventure game!!")
    print("There are two paths ahead:")
    print("1 take the left path")
    print("2 take the right path")

    choice = input("Which path do you choose? (please enter 1 or 2): ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()

def left_path():
    print("You walk along the left path and find a unopened chest.")
    print("Would you like to open it?")
    choice = input("Type yes to open it or no to walk away: ")
    

    if choice.lower() == "yes":
        print("You found a a bow with 4 arrows!")
    else:
        print("You walk away and continue your journey.")

start_adventure()

def right_path():
    print("You take the right path and encounter a sleeping dragon.")
    print("What do you do?")
    print("1 Try to sneak past it.")
    print("2 Attack it with your bow.")

    choice = input("Choose 1 or 2: ")

    if choice == "1":
        print("You successfully sneak past the dragon and find your way to safety. You win!")
    elif choice == "2":
        print("You hit the dragon in the eye and woke it up.The dragon breathes fire! You escape but are wounded.")
    else:
        print("Invalid choice. The dragon wakes up, and you run away in fear!")

start_adventure()