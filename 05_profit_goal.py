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


def profit_goal(total_costs):

    # initialise variables and error message
    error = "Please enter a valid profit goal\n"

    valid = False
    if __name__ == '__main__':
        while not valid:

            # ask for profit goal...
            response = input("What is your profit goal (eg $500 or 50%) ")

            # check if first character is $
            if response[0] == "$":
                profit_type = "$"
                # get amount (everything after the $)
                amount = response [1:]

            # check if last character is %
            elif response [-1] == "%":
                profit_type = "%"
                # get amount (everything after the %)
                amount = response[:-1]

            else:
                # set response to amount for now
                profit_type = "unknown"
                amount = response

            try:
                # check amount is a number more than zero..
                amount = float(amount)
                if amount <= 0:
                    print(error)
                    continue

            except ValueError:
                print(error)
                continue

            if profit_type == "unknown" and amount >= 100:
                dollar_type = yes_no("Do you mean ${:.2f}. ie {:.2f} dollars? , y / n ".format(amount, amount))

                # set profit type based on user answer above
                if dollar_type == "yes" or dollar_type == "y":
                    profit_type = "$"

                else:
                    profit_type = "%"

            elif profit_type == "unknown" and amount < 100:
                percent_type = yes_no("Do you mean {}%? , y / n ".format(amount))

                if percent_type == "yes" or percent_type == "y":
                    profit_type = "%"

                else:
                    profit_type = "$"

            # return profit goal to main routine
            if profit_type == "$":
                return amount
            else:
                goal = (amount / 100) * total_costs
                return goal

# main routine goes here
all_costs = 200

# loop for quick testing...
for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print("Profit Target: ${:.2f}".format(profit_target))
    print("Total Sales: ${:.2f}".format(all_costs + profit_target))
    print()
