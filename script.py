import pandas as pd

# Load the CSV file
file_path = 'path_to_your_csv_file.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Filter items with inventory less than 3
out_of_stock_items = data[data['Variant Inventory Qty'] < 3]

# Calculate the order amount to ensure a minimum quantity of 3
out_of_stock_items['Order Amount'] = 3 - out_of_stock_items['Variant Inventory Qty']

# Select relevant columns for the order
order_columns = ['Image Src', 'Handle', 'Option1 Value', 'Order Amount']
orders_to_place = out_of_stock_items[order_columns]

# Save the orders to a new CSV file
orders_file_path = 'orders_to_place.csv'  # Path where the orders CSV will be saved
orders_to_place.to_csv(orders_file_path, index=False)
