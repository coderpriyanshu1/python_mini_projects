menu = {
    'Pizza':50,
    'Pasta':60,
    'Burger':70,
    'Cold coffee':99,
    'Tanduri Chai':30,
    'Noodles':120,
    'Biryani':220,
}
print("welcome to python restro")
print( "Pizza :50\nPasta :60\nBurger:70\nCold coffee:99\nTanduri Chai:30\nNoodles:120\nBiryani:220")
order_total=0

item_1=input("What do you want to order sir= ")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else: print(f"ordered item {item_1} is not available yet")

another_order=input("Do you want to add another item in your order?(yes/no)")
if another_order=="yes":
    item_2=input("Enter the name of second item")
    if item_2 in menu:
     order_total+=menu[item_2]
     print(f"your item {item_2} has been added to your order")
else:print(f"ordered item {item_2} is not available yet")

print(f"The total amount of your order is {order_total}")
