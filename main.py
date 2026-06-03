class Product:
  def __init__(self, product_id, name, price, quantity):
    self.product_id = product_id
    self.name = name
    self.price = price
    self.quantity = quantity

  def update_stock(self, amount):
    self.amount = amount
    while True:
     if amount < 0:
      stock_debt = amount
      print("{stock_debt} products added to stock to fix negative stock.")
      amount = 0
      print("Stock is now 0.")

     stock_answer = int(input("Do you want to add stock [1] or decrease stock [2]" ))
     if stock_answer == 1:
      stock_add = int(input("How much stock do you want to add? "))
      amount = amount + stock_add
      print("Stock added successfully.")
    
     if stock_answer == 2:
      stock_minus = int(input("How much stock do you want to minus? "))
      amount = amount - stock_minus
      print("Stock minused successfully.")

     else:
      print("Please enter a number.")

  def get_total_value(self, price, quantity):
    total_value = price * quantity
    return total_value
    
  def __str__(self):
    return f"{self.product_id} | {self.name} | ${self.price} | {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = {} # Maps product_id -> Product object

    def add_product(self, product):
        self.products[product.product_id] = product
        # TODO: Add to dictionary
    def restock(product_id, amount, self):
      self.products[product_id].stock_add(amount)

    def sell_product(self, product_id, amount):
      self.products[product_id].stock_minus(-amount)

    def display_all(self):
        return f"{self.products} | {self.name} | ${self.price} | {self.quantity}"
        # TODO: Iterate and print

if __name__ == "__main__": # research what __main__ and __name__ actually does!
    # TODO: Write a while loop to interact with user 
  while True:
    print("Welcome to the Inventory Manager")
    print("1. Add New Product")
    print("2. View All Inventory")
    print("3. Update Product Stock (Buy/Sell)")
    print("4. Exit")
    choice = int(input("Select 1-4: "))
    if choice == 1:
      Inventory.add_product()

    if choice == 2:
      Inventory.display_all()
    
    if choice == 3:
      Product.update_stock()

    if choice == 4:
      break

    else:
      print("Invalid choice")
