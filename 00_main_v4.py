# import libraries
import pandas


# number checkers (checks number is valid)
def num_check(question, error, num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Function doesnt allow blanks for an answer
def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}. \nPlease Try again.\n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# checks that the input is yes or no otherwise prints an error
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


# gets expenses, returns list which has the data frame and sub total
def get_expenses(var_fixed):

    # set up dictionaries
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":
        print()

        # get name, quantity and item
        item_name = not_blank("Item name: ", "The component name cannot be blank.")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = num_check("Quantity: ", "The amount must be a whole number more than zero", int)

        else:
            quantity = 1

        price = num_check("How much for a single item? $", "The price must be a number <more than 0>", float)

        # add item, quantity and price to list
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting  (uses currency fucntion)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


def expenses_print(heading, frame, subtotal):
    print()
    print("**** {} Costs ****".format(heading))
    print(frame)
    print()
    print("{} Costs: ${:.2f}".format(heading, subtotal))
    return ""


# profit goal
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

# *** Main Routine Starts Here ***

# get product name (cant be blank)
product_name = not_blank("Product name: ", "The product name cannot be blank")

print()
print("Please enter your variable costs below...")

# get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes" or have_fixed == "y":
    # get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0



print()
print("*** Fund Raising - {} ***".format(product_name))
print()

expenses_print("Variable", variable_frame, variable_sub)

if have_fixed == "yes" or have_fixed == "y":
    expenses_print("Fixed", fixed_frame, fixed_sub)

print()
print("Total: ${:.2f}".format(fixed_sub + variable_sub))
