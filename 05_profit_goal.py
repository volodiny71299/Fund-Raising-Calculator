# functions go here


def yes_no(question):

    error = "please answer yes/no"

    valid = False
    while not valid:

        # ask question and put response in lowercase
        response = input(question).lower()
        if response == "yes" or response == "y":
            return response
        elif response == "no" or response == "n":
            return response
        else:
            print(error)


def  profit_goal(total_costs):



# main routine goes here
all_costs = 200

# loop for quick testing...
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))
    print()
