import math


# rounding function
def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to

# main routine start here
to_round = [2.75, 2.25, 2]

for item in to_round:
    rounded = round_up(item, 5)
    print("${:.2f} --> ${:.2f}".format(item, rounded))
