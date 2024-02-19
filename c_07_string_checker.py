# checks users enter a valid choice based on a list
# it accepts either the first letter of the full word
# and has a custom error message. (returns the full word)
def choice_checker(question, num_letters, valid_list):

    error = "Please choose {} or {}".format(valid_list[0],
                                            valid_list[1])

    while True:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response == item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[:num_letters] or response == item:
                return item

        # output error if the item not in list
        print(error)
        print()


# main routine goes here

# List for checking responses
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Loop for testing purposes
for case in range(0, 5):
    # Ask the user if they want to read the instructions check it's valid
    want_instructions = choice_checker("Do you want to read the"
                                       " instructions (y/n): ",
                                       1, yes_no_list)

    print("You chose", want_instructions)

for case in range(0, 5):
    pay_method = choice_checker("Choose a payment method"
                                " (cash / credit): ",
                                2, payment_list)

    print("You chose", pay_method)
