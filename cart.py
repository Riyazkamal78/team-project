"""Demonstrate adding a product to a shopping cart."""

def add_item(cart, product):
    cart.append(product)


if __name__ == "__main__":
    cart = []
    add_item(cart, "Milk")
    print("Cart:", ", ".join(cart))
