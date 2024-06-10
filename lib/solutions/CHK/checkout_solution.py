from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Skus is a string containing all the products of the checkout
    # Return is an integer representing the total checkout value

    # Input validation
    if not isinstance(skus, str):
        return -1
    
    # Dictionary for offers and prices
    offers = {
        "A": (3, 130),
        "B": (2, 45)
    }

    prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    # Checkout_quantity keeps track of the quantity of this 
    # product within the basket 
    checkout_quantity = defaultdict(int)
    for product in skus:
        if product in prices:
            checkout_quantity[product]+=1
        else:
            return -1
    
    total = 0
    for product in checkout_quantity.keys():
        # Calculate the cost on special offer
        if product in offers:
            while checkout_quantity[product] >= offers[product][0]:
                # Incrementing total by offer and reducing the checkout quantity
                total+= offers[product][1]
                checkout_quantity[product] -= offers[product][0]
            
        if checkout_quantity[product] > 0:
            total += checkout_quantity[product]*prices[product]
    
    return total


    
