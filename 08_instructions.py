

# string checker, checks user input is valid by comparing input with options in a list
# used for yes / no questions and also to check valid snacks have been chosen
def string_check(choice, options):

    for var_list in options:

        # if the snack is in one of the lists, return the full
        if choice in var_list:

            # get full name of snack and put it in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not ok - ask question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# outputs instructions if users have not used the program before
def instructions(option):
    show_help = "invalid choice"
    while show_help == "invalid choice":
        show_help = input("Would you like to read the instructions for this program? ").lower()
        show_help = string_check(show_help, option)
        if show_help == "invalid choice":
            print("Please reply with y/n")

    if show_help == "Yes":
        print()
        print("*** Mega Movie Fundraiser Instructions ***")
        print()
        print("Instructions go here. They are brief but helpful")

    return ""

yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

# ask user if they have used the program before and show instructions
instructions(yes_no)
