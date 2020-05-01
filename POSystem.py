

class Inventory:
    def __init__(self):
        self._inventory = {}

    def get_inventory(self):
        return self._inventory

    def set_inventory(self, product_name, price, qty, product_id):
        self._inventory.update({product_name: [price, qty, product_id]})

    def check_inventory(self, product_name):
        for key in self._inventory.keys():
            if product_name == key:
                return f'Product Available, we have {self._inventory.get(product_name)[1]} left'


class Register:
    def __init__(self, cash=1000):
        self._cash = cash

    def drawer(self):
        return self._cash


class Checkout(Inventory, Register):
    def __init__(self):
        self._cart = {}
        self._total = 0
        super().__init__()

    def add_to_cart(self, product_name, qty):
        for key in self._inventory.keys():
            if product_name == key:
                self._cart.update({product_name: qty})
                self._total += self._cart.get(product_name)[1]

    def get_total(self):
        return self._total

    def check_out(self, amount_paid):
        if self._total < amount_paid:
            change = amount_paid - self._total
            print(f'Thank You, your change is {change}')

