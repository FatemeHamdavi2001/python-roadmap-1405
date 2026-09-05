product1 = float(input("Enter price product1: "))
product2 = float(input("Enter price product2: "))
product3 = float(input("Enter price product3: "))
Subtotal = product1 + product2 + product3
Discount = Subtotal * 0.1
Final_price = Subtotal - Discount
if Subtotal > 200 :
    print("final price with discount = ", Final_price)
else :
    print("final price without discount = ", Subtotal)