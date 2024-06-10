from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Skus is a string containing all the products of the checkout
    # Return is an integer representing the total checkout value

    # Input validation
    if not isinstance(skus, str):
        return -1
    
    # Dictionary of lists of offers and prices
    # TODO Define a hirerarchy of offers, greatest to lowest
    # Potentially define a topological sort to check which offers have an impact on others
    # Given the offer list is so small this may be overkill
    offers = {
        "A": [(3, 130), (5,200)],
        "B": [(2, 45)],
        "E": [(2, "B")]
        
    }

    prices = {
        "E": 40,
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
            while checkout_quantity[product] >= offers[product][0][0]:
                # Getting a better offer by checking quantity against other offers for this product
                current_offer = offers[product][0]
                idx = 0
                while len(offers[product]) > (idx +1) and checkout_quantity[product] >= offers[product][idx+1][0]:
                    idx+=1
                    current_offer = offers[product][idx]
                # Evaluate Offer
                if isinstance(current_offer[1], int):
                    # Incrementing total by offer and reducing the checkout quantity
                    total+= current_offer[1]
                else:
                    # Offer is discount on another product
                    # Updat the total, reduce quantity of the other product
                    total+=prices[product]*current_offer[0]
                    if checkout_quantity[current_offer[1]] > 0:
                        checkout_quantity[current_offer[1]] -=1
                checkout_quantity[product] -= current_offer[0]
            
        if checkout_quantity[product] > 0:
            total += checkout_quantity[product]*prices[product]
    
    return total


    

