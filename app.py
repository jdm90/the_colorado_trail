import sys
import travel_the_trail

def game_menu(name):
    print("")
    print("       === The Colorado Trail ===       \n")
    print(f"Welcome {name}!\n")
    print("Game Menu")
    print("------------------------------------------")
    print("| 1. Travel the trail")
    print("| 2. Learn about the trail")
    print("| 3. Quit")
    print("------------------------------------------")

print("*** THE COLORADO TRAIL GAME ***")
print("Created with Python by n1ftyn0m4d © 2022\n")

name = input("What is your name? ")

game_menu(name)

game_menu_input = input("What is your choice? ")

if game_menu_input == "1":
    print(f"\nOk {name}, let's hit it!")
    for num in range(3, 0, -1):
        print(num)
    print("And we're off...")    
elif game_menu_input == "2":
    print("\nThe Colorado Trail is a long distance trail The Colorado Trail is a long-distance trail running for 486 miles from the mouth of Waterton Canyon southwest of Denver to Durango in Colorado, USA.")
    print("Its highest point is 13,271 feet above sea level, and most of the trail is above 10,000 feet.")
    print("The trail was completed in the year 1987.")
    print("It was built and is currently maintained by the non-profit Colorado Trail Foundation and the United States Forest Service.")
    print("The Colorado Trail and the Continental Divide Trail follow the same path for approx. 200 miles.\n")
    print("Thanks for choosing to learn more about the Colorado Trail!\n")
    print("------------------------------------------")
    print("| 1. Travel the trail")
    print("| 2. Quit")
    print("------------------------------------------")
    game_menu_input = input("What would you like to do next? ")
    if game_menu_input == "1":
        print(f"\nOk {name}, let's hit it!")
        for num in range(3, 0, -1):
            print(num)
        print("And we're off...")
    else:
        sys.exit(f"\nGoodbye {name}!\nCatch you next time.\n")
else:
    sys.exit(f"\nGoodbye {name}!\nCatch you next time.\n")