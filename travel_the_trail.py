def game():
    print("\nIt's a beautiful day in Littleton, Colorado.")
    print("Your best friend Curtis has just dropped you off at a popular trailhead for embarking on this incredible journey.\n")

    has_dog = input("Are you bringing a furry pal? Type 'yes' to bring your dog, or 'no' to leave him with your good pal, Curtis. ")
    if has_dog == "yes":
        has_dog = True
        dogs_name = input("What is your dog's name? ")
    elif has_dog == "no":
        has_dog = False
    else:
        print("Error: invalid response")

    pack_size = input("What size pack will you be traveling with... 'small', 'medium', or 'large'? ")
    
