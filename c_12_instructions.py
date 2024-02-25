# Function go here...
# check user answers yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


# Display instructions
def show_instructions():
    print('''\n
    ***** Instructions *****
    For each ticket, enter...
    - The person's name (can't be blank)
    - Age (between 12 and 120)
    - Payment method (cash / credit)

    When you have entered all the users, press 'xxx' to quit.

    The program will then display the ticket details 
    including the cost of each ticket, the total cost
    and the total profit.

    This information will also be automatically written to
    a text file.

    *****************************''')


# Main Routine goes here...
played_before = yes_no("Have you played the "
                       "game before?  ")

if played_before == "no":
    show_instructions()
print()
print("Please press <enter> to begin...")