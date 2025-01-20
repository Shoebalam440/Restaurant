
menue={
    'chai':10,
    'coffee':5,
    'pizza':60,
    'dosa':30,
    'samosa':15
}

#greet
print("Welcome to ALAM Restuarant \U0001F64F")
print("Chai: Rs 10\- \nCoffee: Rs 5\- \nPizza: Rs 60\- \nDosa: Rs 30\- \nSamosa: Rs 15\-")


order_total= 0

item_1=input("Enter the name of item you want to order=")
if item_1 in menue:
    order_total +=menue[item_1]
    print(f'your item {item_1} has been added to your order')

else:
    print(f"Your ordered item {item_1 } not available")

another_order=input("Do you want to order another item (Yes/No)")
if another_order=="yes":
    item_2=input("Enter the name of second item=")
    if item_2 in menue:
        order_total+=menue[item_2]
        print(f"your item {item_2} has been added to your order")
    else:
        print(f"Your ordered item {item_2 } not available")

print(f"Total Amount = Rs{order_total}\-")