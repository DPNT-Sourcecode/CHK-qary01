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
    # NOTE The offers can be the new price of this quantity or a free item 
    # The structure is a list of offers (tuples) on a sku where the first element is the quantity
    # required and the second element is the discount either the price for those items or the sku which is free
    # Potentially define a topological sort to check which offers have an impact on others
    # Given the offer list is so small this is probably overkill but may be nessisary in the future
    # If offers become more complex
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
    # TODO
    # Traversing through the prices, adds unnessisary compute in a supermarket with a lot of products
    # For now without using a topological sort this is a workaround given the time strain on this exercise
    # If time allows, we can optimise this later to reduce unnesisary work
    for product in prices.keys():

        if product not in checkout_quantity:
            continue
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
                    if current_offer[1] in checkout_quantity and checkout_quantity[current_offer[1]] > 0:
                        checkout_quantity[current_offer[1]] -= 1
                checkout_quantity[product] -= current_offer[0]
            
        if checkout_quantity[product] > 0:
            total += checkout_quantity[product]*prices[product]
    
    return total


    


