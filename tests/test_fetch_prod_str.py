import pytest

from lib.fetch_input import fetch_product_sum, fetch_is_prod_imported, fetch_prod_price

#normal prod str
@pytest.fixture
def prod_inputs():
    prod_a = "1 book at 12.49"
    prod_b = "5 music CD at 14.99"
    return [prod_a, prod_b]

#imported prod str
@pytest.fixture
def prod_imported_inputs():
    prod_a = "1 book imported at 12.49"
    prod_b = "5 imported music CD at 14.99"
    prod_c = "2 music CD at 14.99"
    return [prod_a, prod_b, prod_c]

class TestTaxCaculator:
    #test fetch sum of correct str
    def test_fetch_sum(self, prod_inputs):
        sum = fetch_product_sum(prod_inputs[0])
        assert sum == 1

        sum = fetch_product_sum(prod_inputs[1])
        assert sum == 5
    
    def test_fetch_prod_is_imported(self, prod_imported_inputs):
        is_imported = fetch_is_prod_imported(prod_imported_inputs[0])
        assert is_imported == True

        is_imported = fetch_is_prod_imported(prod_imported_inputs[1])
        assert is_imported == True

        is_imported = fetch_is_prod_imported(prod_imported_inputs[2])
        assert is_imported == False

    def test_fetch_prod_price(self, prod_inputs):
        price = fetch_prod_price(prod_inputs[0])
        assert price == 12.49

        price = fetch_prod_price(prod_inputs[1])
        assert price == 14.99
