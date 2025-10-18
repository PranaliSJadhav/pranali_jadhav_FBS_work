cost_price = int(input("enter cost price of book:"))
discount = int(input("enter discount price in percentage:"))

discount_amount = cost_price * discount  / 100
selling_price = cost_price - discount_amount

print("selling price based on cost price and discount ",selling_price)
