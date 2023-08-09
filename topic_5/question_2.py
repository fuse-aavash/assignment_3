class FoodItem:
    """
    Represents a food item with a name and price.

    Attributes:
        name (str): The name of the food item.
        price (float): The price of the food item.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    """
    Represents a restaurant with a name and a menu of food items.

    Attributes:
        name (str): The name of the restaurant.
        menu (dict): A dictionary containing food items as keys and their quantities as values.

    Methods:
        add_to_menu(food_item, quantity): Add a food item with a certain quantity to the menu.
        remove_from_menu(food_item, quantity): Remove a certain quantity of a food item from the menu.
        get_total_revenue(): Calculate the total revenue generated from the menu.
    """
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_to_menu(self, food_item, quantity):
        """Add a food item with a certain quantity to the menu."""
        if quantity >= 0:
            if food_item in self.menu:
                self.menu[food_item] += quantity
            else:
                self.menu[food_item] = quantity
        else:
            print("Invalid quantity value. Quantity cannot be negative.")

    def remove_from_menu(self, food_item, quantity):
        """Remove a certain quantity of a food item from the menu."""
        if food_item in self.menu:
            if quantity >= 0:
                if self.menu[food_item] <= quantity:
                    del self.menu[food_item]
                else:
                    self.menu[food_item] -= quantity
            else:
                print("Invalid quantity value. Quantity cannot be negative.")
        else:
            print(f"{food_item.name} not found in the menu.")

    def get_total_revenue(self):
        """Calculate the total revenue generated from the menu."""
        total_revenue = 0
        for food_item, quantity in self.menu.items():
            total_revenue += food_item.price * quantity
        return total_revenue

class Customer:
    """
    Represents a customer with a name, address, and a cart of food items.

    Attributes:
        name (str): The name of the customer.
        address (str): The address of the customer.
        cart (dict): A dictionary containing food items as keys and their quantities as values.

    Methods:
        add_to_cart(food_item, quantity): Add a food item with a certain quantity to the customer's cart.
        remove_from_cart(food_item, quantity): Remove a certain quantity of a food item from the customer's cart.
    """
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cart = {}

    def add_to_cart(self, food_item, quantity):
        """Add a food item with a certain quantity to the customer's cart."""
        if quantity > 0:
            if food_item in self.cart:
                self.cart[food_item] += quantity
            else:
                self.cart[food_item] = quantity
        else:
            print("Quantity must be greater than zero.")

    def remove_from_cart(self, food_item, quantity):
        """Remove a certain quantity of a food item from the customer's cart."""
        if food_item in self.cart:
            if quantity >= 0:
                if self.cart[food_item] <= quantity:
                    del self.cart[food_item]
                else:
                    self.cart[food_item] -= quantity
            else:
                print("Invalid quantity value. Quantity cannot be negative.")
        else:
            print(f"{food_item.name} not found in the cart.")

class DeliveryService:
    """
    Represents a delivery service that manages a list of restaurants.

    Attributes:
        restaurants (list): A list containing Restaurant objects.

    Methods:
        add_restaurant(restaurant): Add a restaurant to the list of managed restaurants.
        find_restaurant_by_name(name): Find a restaurant by its name in the list.
    """
    def __init__(self):
        self.restaurants = []

    def add_restaurant(self, restaurant):
        """Add a restaurant to the list of managed restaurants."""
        self.restaurants.append(restaurant)

    def find_restaurant_by_name(self, name):
        """
        Find a restaurant by its name in the list.

        Args:
            name (str): The name of the restaurant to search for.

        Returns:
            Restaurant or None: The found restaurant or None if not found.
        """
        for restaurant in self.restaurants:
            if restaurant.name == name:
                return restaurant
        return None

# Test the food delivery system
restaurant1 = Restaurant("Tasty Bites")
restaurant2 = Restaurant("Spice Delight")

food_item1 = FoodItem("Burger", 8)
food_item2 = FoodItem("Pizza", 12)
food_item3 = FoodItem("Pasta", 10)

restaurant1.add_to_menu(food_item1, 10)
restaurant1.add_to_menu(food_item2, 5)

restaurant2.add_to_menu(food_item2, 8)
restaurant2.add_to_menu(food_item3, 12)

customer = Customer("Alice", "123 Main St.")
customer.add_to_cart(food_item1, 2)
customer.add_to_cart(food_item2, 3)
customer.add_to_cart(food_item3, -2)  # This should now give an error

delivery_service = DeliveryService()
delivery_service.add_restaurant(restaurant1)
delivery_service.add_restaurant(restaurant2)

restaurant1.remove_from_menu(food_item2, 6)  # This should now give an error
restaurant2.remove_from_menu(food_item1, 1)  # This should now give an error

print("Total revenue for Tasty Bites:", restaurant1.get_total_revenue())
print("Total revenue for Spice Delight:", restaurant2.get_total_revenue())
