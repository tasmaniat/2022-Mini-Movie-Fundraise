import pandas
import random
from datetime import date


# Functions go here

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


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here

# set maximum number of tickets below
MAX_TICKETS = 5

# List for checking responses
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold tickets details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data fra,e ie: colum_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask the user if they want to read the instructions  and check it's valid
want_instructions = choice_checker("Do you want to read the"
                                   " instructions (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    print(show_instructions())

print()

# loop to sell tickets
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    # exit loop if users type 'xxx' and have sold at least
    # one ticket
    if name == 'xxx' and len(all_names) > 0:
        break
    elif name == 'xxx':
        print("You must sell at least ONE Ticket before quitting")

    age = num_check("Age: ")

    # Checks if user is between 12 and 120 (inclusive)
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

    # Get payment method
    pay_method = choice_checker("Choose a payment method"
                                " (cash / credit): ",
                                2, payment_list)

    print(f"you are paying {pay_method}")

    if pay_method == "cash":
        surcharge = 0
    else:
        # calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # add ticket name cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']

# calculate the profit for each ticket
mini_movie_frame["Profit"] = mini_movie_frame['Ticket Price'] - 5

# calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# choose a winner and look up total won
winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "\n---- Mini Movie Fundraiser Ticket Data ({}/{}/{}) ----\n".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to string so that we can export it to file
mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

# create string for printing...
ticket_cost_heading = "\n----- Ticket Cost / Profit -----"
total_ticket_sales = "Total Tickets Sales: ${:.2f}".format(total)
total_profit = "Total Profit : ${:.2f}".format(profit)

# show users how many tickets hve been sold
if tickets_sold == MAX_TICKETS:
    sales_status = "\n*** All the tickets have been sold ***"
else:
    sales_status = "\n **** You have old {} out of {} " \
                   "tickets *****".format(tickets_sold, MAX_TICKETS)

# Output Raffle results
winner_heading = "\n---- Raffle Winner ----"
winner_text = "The winner of the raffle is {}. " \
              "They have won ${:.2f}. ie: Their ticket is " \
              "free!".format(winner_name, total_won)

# list holding content to print / write to file
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
