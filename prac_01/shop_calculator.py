total = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of items: "))
total_items = items
while items > 0:
    cost = float(input("Price of item: "))
    total = total + cost
    items = items - 1
if total > 100:
    total = total - (total * 0.1)
print("Total price for " + str(total_items) + " items is $" + format(total, '.2f'))
