# Week03 Lab03 - Q2


cart =["apple", "banana", "milk", "bread", "apple", "eggs"]
apple_count = cart.count("apple")
print(f"Number of apples: {apple_count}")
milk_position = cart.index("milk")
print(f"Position of milk: {milk_position}")

cart.remove("apple") # removes the first occurrence of "apple" from left to right

print(f"Remove item using pop: {cart.pop()}")
print("Is 'banana' in cart?", "banana" in cart)
print(f"Final cart cart: {cart}")
