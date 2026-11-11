customer_name = input("Enter customer name: ").strip()

products = []
for i in range(1, 4):
    product_name = input(f"Enter product {i} name: ").strip()
    product_price = float(input(f"Enter price for {product_name}: "))
    products.append((product_name, product_price))

subtotal = sum(price for _, price in products)

if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.00

discount = subtotal * discount_rate
final_total = subtotal - discount

print(f"Customer Name: {customer_name}")
print()
for i, (name, price) in enumerate(products, start=1):
    print(f"Product {i}: {name}")
    print(f"Price: {price:.0f}")
    print()

print(f"Subtotal: {subtotal:.0f}")
print(f"Discount: {discount:.0f}")
print(f"Final Total: {final_total:.0f}")
