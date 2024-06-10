from solutions.CHK.checkout_solution import checkout


class TestCheckout():

    def test_checkout(self):
        '''Test checkout with normal input'''
        assert checkout("AA") == 100
    
    def test_bad_input(self):
        '''Test checkout with bad input'''
        assert checkout(50) == -1
    
    def test_checkout_offer(self):
        '''Test that an offer corrects the total price for checkout'''
        assert checkout("AAA") == 130
    
    def test_checkout_higher_quantity_offer(self):
        '''Test that an offer corrects the total price for checkout'''
        assert checkout("AAAAA") == 200
    
    def test_checkout_multi_offer_offer(self):
        '''Test that an offer corrects the total price for checkout'''
        assert checkout("AAAAAAAA") == 330
    
    def test_checkout_multi_offer_with_quantity_offer(self):
        '''Test that an offer corrects the total price for checkout'''
        assert checkout("AAAAAAAAA") == 380
    
    def test_checkout_offer_with_excess(self):
        '''Test that an offer reduces the price and products not meeting the threshold will
        be added to total at regular price'''
        assert checkout("AAAA") == 180
    
    def test_checkout_sku_not_in_inventory(self):
        '''Test unexpected sku not in inventory results in -1 response'''
        assert checkout("F") == -1
    
    def test_checkout_product_combo_of_sku_in_and_not_in_inventory(self):
        '''Test unexpected sku in an otherwise valid basket will result in -1 response'''
        assert checkout("AF") == -1
    
    def test_checkout_all_skus(self):
        '''Test all skus come to correct total'''
        assert checkout("ABCD") == 115
    
    def test_checkout_product_multi_offer_checkout(self):
        '''Test products added to basket in various order will still trigger offers'''
        assert checkout("ABCDBAA") == 210
    
    def test_checkout_discount_on_other_sku_checkout(self):
        '''Test enough quantity of sku will result less quantity of another sku'''
        assert checkout("EEB") == 80
    
    def test_checkout_discount_on_other_sku_checkout_stops_offer(self):
        '''Test enough quantity of sku will result less quantity of another sku'''
        assert checkout("EEBB") == 110
    
    def test_checkout_discount_on_other_sku_with_no_quantity(self):
        '''Test enough quantity of sku will compute even if there is no sku to remove'''
        assert checkout("EE") == 80
    
    def test_checkout_1(self):
        '''Test enough quantity of sku will result less quantity of another sku'''
        assert checkout("BEBEEE") == 160

    def test_checkout_2(self):
        '''Test enough quantity of sku will result less quantity of another sku'''
        assert checkout("ABCDEABCDE") == 280
    

    def test_checkout_3(self):
        '''Test enough quantity of sku will result less quantity of another sku'''
        assert checkout("ABCDEABCDE") == 665
