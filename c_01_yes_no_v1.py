show_instructions = ""
while show_instructions.lower() != "xxx":
    # ask the user if they have played the game before.
    show_instructions = input("Have you played "
                              "before? ").lower()

    # if they say yes, output 'program continues'
    # if they say no, output 'display instructions'
    # if the answer is invalid, print an error.

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")
        print()
    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")
        print()
    elif show_instructions == "n":
        print("display instructions")

    else:
        print("please answer yes/no")
        print()
