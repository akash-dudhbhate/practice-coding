"""SOLUTION: ShoppingCart Class (Hard)"""
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append((name, price))

    def total(self):
        return sum(price for _, price in self.items)

    def remove_item(self, name):
        for i, (n, _) in enumerate(self.items):
            if n == name:
                self.items.pop(i)
                return

    def __str__(self):
        items_str = "\n".join(f"  {n}: ${p}" for n, p in self.items)
        return f"Cart:\n{items_str}\nTotal: ${self.total()}"

if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("apple", 1.5)
    cart.add_item("bread", 3.0)
    assert cart.total() == 4.5
    cart.remove_item("apple")
    assert cart.total() == 3.0
    print("All tests passed!")
