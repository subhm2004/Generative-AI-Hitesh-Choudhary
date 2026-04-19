order_amount = int(input("Enter the order amount: "))

if(order_amount > 150):
    delivery_charge = 0
else:
    delivery_charge = 30
    
print(f"Delivery fees is : {delivery_charge}")