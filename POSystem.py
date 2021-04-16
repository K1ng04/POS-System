
class Sales():
    def __init__(self):
        self.Sales = {}
    def get_sale(self):
        return self.Sales
    def set_Sales(self, name, price ,quantity):
        self.Sales = {name: {"Price": price, "Quantity": quantity}}
class Inventory(Sales):
    def __init__(self):
        super().__init__()
        self.Inventory = {}
    def set_Inventory(self, name, price, quant):
        self.Inventory[name] = {"Price": price, "Quantity": quant}
    def get_Inventory(self):
        return self.Inventory
    def remove_Inventory(self, name, quantity):
        if self.Inventory.get(name) != None:
            self.Sales[name] = {"Product": name, "Quantity": quantity} 
            if self.Inventory[name]["Quantity"] == 1:
                print(f'There is only {self.Inventory[name]["Quantity"]} left')
                ans = input("Would you like to Continue (Y/N): ")
                if ans.upper() == 'Y' or ans.upper == "YES":
                    self.Inventory[name]["Quantity"] -= quantity 
                    price = self.Inventory[name]["Price"]
                    Sales.set_Sales(self, name, price, quantity)
                    self.Inventory.pop(f'{name}', None)
            elif self.Inventory[name]["Quantity"] > 1: 
                price = self.Inventory[name]["Price"]
                Sales().set_Sales(name, price, quantity)
                self.Inventory[name]["Quantity"] -= quantity
            else:
                 print(f'{name} does not exist in the inventory')
        else:
            print(f'{name} does not exist in the inventory')





# class Checkout(Inventory): 

y = Inventory()
y.set_Inventory('Rolex', 15000,2)
y.set_Inventory('Patek Philippe', 100000, 1)
y.set_Inventory('Hublot', 50000, 5)
y.set_Inventory('Richard Mille', 100000, 5)
print(y.get_Inventory())
y.remove_Inventory('Richard Mille', 4)
print(y.get_Inventory())
print(y.get_sale())