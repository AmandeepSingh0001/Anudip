def calculate_discounted_price(cost_price, discount_percentage=20):
    """Calculates the discounted price of an item."""
    discount = (discount_percentage / 100) * cost_price
    discounted_price = cost_price - discount
    return discounted_price

if __name__ == "__main__":
    cost_price = float(input("Enter the cost price of the item: "))
    discounted_price = calculate_discounted_price(cost_price)
    print("The discounted price is:", discounted_price)