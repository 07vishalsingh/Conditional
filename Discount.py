def calculate_discount(price, discount_percentage):
    """Calculates the discounted price based on a given percentage.

    Args:
        price (float): The original price.
        discount_percentage (float): The discount percentage (0-100).

    Returns:
        float: The discounted price.
    """

    if not 0 <= discount_percentage <= 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    discount = price * (discount_percentage / 100)
    discounted_price = price - discount
    return discounted_price

# Example usage
price = 50.00
discount_percentage = 20.00

try:
    discounted_price = calculate_discount(price, discount_percentage)
    print(f"The original price is ${price:.2f}, with a discount of {discount_percentage:.2f}%, the final price is ${discounted_price:.2f}.")
except ValueError as e:
    print(e)
