from typing import List
class Product:
    def __init__(self, price: float):
        """
        Represents a generic product.

        Args:
            price (float): The price of the product.

        Attributes:
            price (float): The price of the product.
        """
        self.price = price

    def get_price(self) -> float:
        """
        Get the price of the product.

        Returns:
            float: The price of the product.
        """
        return self.price


class DiscountedProduct(Product):
    def __init__(self, price: float, discount: float):
        """
        Represents a product with a discount.

        Args:
            price (float): The price of the product before discount.
            discount (float): The discount amount as a percentage (e.g., 0.1 for 10% discount).

        Attributes:
            price (float): The price of the product before discount.
            discount (float): The discount amount as a percentage.
        """
        super().__init__(price)
        self.discount = discount

    def get_price(self) -> float:
        """
        Get the price of the product after applying the discount.

        Returns:
            float: The discounted price of the product.
        """
        return self.price * (1 - self.discount)


def calculate_total_price(products: List[Product]) -> float:
    """
    Calculate the total price of a list of products.

    Args:
        products (list[Product]): A list of Product objects.

    Returns:
        float: The total price of all products in the list.
    """
    total_price = 0
    for product in products:
        total_price += product.get_price()
    return total_price


# Using the calculate_total_price function with a list of products
products = [Product(100), Product(50), DiscountedProduct(75, 0.1)]
print("Total Price:", calculate_total_price(products))

