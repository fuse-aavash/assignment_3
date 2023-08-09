class Product:
    """
    Represents a product with a name, price, and quantity.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product.

    Methods:
        get_total_price(): Calculate the total price of the product based on its price and quantity.
        update_quantity(new_quantity): Update the quantity of the product, ensuring it's not negative.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        """Calculate the total price of the product."""
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        """
        Update the quantity of the product.

        Args:
            new_quantity (int): The new quantity value for the product.

        Note:
            Negative values for new_quantity are not allowed.
        """
        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            print("Invalid quantity value. Quantity cannot be negative.")

class ShoppingCart:
    """
    Represents a shopping cart containing products and their quantities.

    Attributes:
        products (dict): A dictionary containing products as keys and their quantities as values.

    Methods:
        add_product(product, quantity): Add a product with a given quantity to the cart.
        remove_product(product, quantity): Remove a certain quantity of a product from the cart.
        get_total_cart_price(): Calculate the total price of all products in the cart.
    """
    def __init__(self):
        self.products = {}

    def add_product(self, product, quantity):
        """
        Add a product with a given quantity to the cart.

        Args:
            product (Product): The product to be added to the cart.
            quantity (int): The quantity of the product to be added.

        Note:
            Negative values for quantity are not allowed.
        """
        if quantity >= 0:
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity
        else:
            print("Invalid quantity value. Quantity cannot be negative.")

    def remove_product(self, product, quantity):
        """
        Remove a certain quantity of a product from the cart.

        Args:
            product (Product): The product to be removed from the cart.
            quantity (int): The quantity of the product to be removed.

        Note:
            Negative values for quantity are not allowed.
        """
        if product in self.products:
            if quantity >= 0:
                if self.products[product] <= quantity:
                    del self.products[product]
                else:
                    self.products[product] -= quantity
            else:
                print("Invalid quantity value. Quantity cannot be negative.")
        else:
            print("Product not found in the cart.")

    def get_total_cart_price(self):
        """Calculate the total price of all products in the cart."""
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.get_total_price() * quantity
        return total_price

class Customer:
    """
    Represents a customer with a name, email, and a shopping cart.

    Attributes:
        name (str): The name of the customer.
        email (str): The email address of the customer.
        shopping_cart (ShoppingCart): The shopping cart associated with the customer.

    Methods:
        add_to_cart(product, quantity): Add a product with a certain quantity to the customer's cart.
        remove_from_cart(product, quantity): Remove a certain quantity of a product from the customer's cart.
        checkout(): Proceed to checkout the items in the customer's cart.
    """
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shopping_cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        """Add a product with a certain quantity to the customer's cart."""
        self.shopping_cart.add_product(product, quantity)

    def remove_from_cart(self, product, quantity):
        """Remove a certain quantity of a product from the customer's cart."""
        self.shopping_cart.remove_product(product, quantity)

    def checkout(self):
        """Proceed to checkout the items in the customer's cart."""
        total_price = self.shopping_cart.get_total_cart_price()
        if total_price > 0:
            print(f"Checking out... Your total is ${total_price}.")
            self.shopping_cart.products = {}
        else:
            print("Your cart is empty. Nothing to checkout.")

# Test the e-commerce system
product1 = Product("Keyboard", 50, 2)
product2 = Product("Mouse", 30, 3)

customer = Customer("John Doe", "john.doe@example.com")
customer.add_to_cart(product1, 1)
customer.add_to_cart(product2, 2)
customer.checkout()

customer.add_to_cart(product1, -1)  # This should now give an error
customer.remove_from_cart(product2, 3)  # This should now give an error
