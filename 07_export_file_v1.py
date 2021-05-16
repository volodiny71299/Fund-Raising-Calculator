import pandas

# frames and content for export

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5,.75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Adcertising"],
    "Price": [25, 30, 10],
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "$5.00"

print(variable_frame)

# change dataframe to string (so it can written to a txt file)
variable