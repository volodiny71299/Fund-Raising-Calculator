import math


# integer that is more than zero (has custom error message)
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


# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

# main routine start here
how_many = num_check("How many items? ", "Can't be 0", int)
total = num_check("Total costs? ", "More than 0", int)
profit_goal = num_check("Profit goal? ", "More than 0", int)
round_to = num_check("Round to nearest...? ", "Can't be 0", int)

sales_needed = total + profit_goal

print("Total: ${:.2f}".format(total))
print("Profit Goal: ${:.2f}".format(profit_goal))

selling_price = sales_needed / how_many
print("Selling price (unrounded): {:.2f}".format(selling_price))

recommended_price = round_up(selling_price, round_to)
print("Recommended Price: ${:.2f}".format(recommended_price))
