# checks that number is valid in float string


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

# main routine goes here
get_int = num_check("How many do you need? ", "Please enter an amount more than 0\n", int)

get_cost = num_check("How much does it cost? $", "Please enter a number more than 0\n", float)
