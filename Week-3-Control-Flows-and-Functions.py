    # Function creation
def calculate_discount(price, discount_percent):
    # If the discount is 20% or higher, calculate and return the discounted price.
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    # Otherwise, return the original price.
    else:
        return price
try:
    # user input for price and discount percentage.
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # final price after applying the discount.
    final_price = calculate_discount(price, discount_percent)
    
    # Check if discount was applied and print the result.
    if discount_percent >= 20:
        print(f"Final price after discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {price:.2f}")
except ValueError:
    print("Invalid input. Please enter numbers for the price and discount.")
