class Product:
    def __init__(self, name, price):
        self.price = price
        self.category = "general"
        self.name = name

    def print_info(self):
        print(f"The product: {self.name}\nCategory: {self.category}\nPrice: {self.price}")
        return self

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += self.price * (percent_change / 100)
        else:
            self.price -= self.price * (percent_change / 100)
        return self

    def inflation(self, inflation_rate):
        self.price += self.price * (inflation_rate / 100)
        return self

    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"

class Store:
    def __init__(self, name="mystore"):
        self.name = name
        self.product_list = []

    def add_product(self, new_product):
        self.product_list.append(new_product)
        print(f"{new_product} added to {self.name}")
        return self

    def sell_product(self, id):
        if 0 <= id < len(self.product_list):
            sold_product = self.product_list.pop(id)
            print(f"{sold_product} sold from {self.name}")
        else:
            print(f"Product ID {id} not found in {self.name}")
        return self

    def apply_inflation(self, inflation_rate):
        for product in self.product_list:
            product.inflation(inflation_rate)
        print("inflation applied")
        return self


store = Store()

laptop = Product("laptop", 1000)
biscuit = Product("biscuit", 20)
parfum = Product("parfum", 200)

# store.add_product(laptop)
# store.add_product(biscuit)
# store.add_product(parfum)

store.apply_inflation(1)

# laptop.update_price(2, True).print_info()
