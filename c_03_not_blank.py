# functions goes here
def not_black(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be black. Please try again")
        else:
            return response

# main routine goes here

