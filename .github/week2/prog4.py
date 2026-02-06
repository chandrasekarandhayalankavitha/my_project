
def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total

# Only positional
print("bill :",calculate_bill(100, 2))
# With custom tax
print("bill :",calculate_bill(100, 2, tax=0.7))
# With custom discount
print("bill :",calculate_bill(100, 2, discount=15))
# With both custom tax and discount
print("bill :",calculate_bill(100, 2, tax=0.7, discount=15))