# Functions go here

# checks that user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be black. Please try again")
        else:
            return response


# checks users enter an integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):
    # ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # ticket is 10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# checks users enter a valid choice based on a list
# it accepts either the first letter of the full word
# and has a custom error message. (returns the full word)
def choice_checker(question, num_letters, valid_list):
    error = "Please choose {} or {}".format(valid_list[0],
                                            valid_list[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response == item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[:short_version] or response == item:
                return item

        # output error if the item not in list
        print(error)
        print()


# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 3

# List for checking responses
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Ask the user if they want to read the instructions  and check it's valid
want_instructions = choice_checker("Do you want to read the"
                                   " instructions (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    print("Instructions go here")

print()

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue

    # calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    pay_method = choice_checker("Choose a payment method"
                                " (cash / credit): ",
                                2, payment_list)

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s"
          " remaining".format(tickets_sold, MAX_TICKETS - tickets_sold))
