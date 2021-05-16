import pandas

# frames and content for export

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Advertising"],
    "Price": [25, 30, 10],
}

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

# change frames to strings
variable_txt = pandas.DataFrame.to_string(variable_frame)
fixed_txt = pandas.DataFrame.to_string(fixed_frame)

product_name = "Custom Mugs"
profit_target = "$100.00"
required_sales = "$200.00"
recommended_price = "The recommended price is $5.00"

print(variable_frame)

to_write = [product_name, variable_txt, fixed_txt, profit_target, required_sales, recommended_price]

# write to file...
# create file to hold data (add .txt extension
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# close file
text_file.close()

# print stuff
for item in to_write:
    print(item)
    print()
