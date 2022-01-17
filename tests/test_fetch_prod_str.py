import pytest

from lib.fetch_input import fetch_product_sum

@pytest.fixture
def prod_inputs():
    prod_a = "1 book at 12.49"
    prod_b = "5 music CD at 14.99"
    return [prod_a, prod_b]

class TestTaxCaculator:
    #test fetch sum of correct str
    def test_fetch_sum(self, prod_inputs):
        sum = fetch_product_sum(prod_inputs[0])
        assert sum == 1

        sum = fetch_product_sum(prod_inputs[1])
        assert sum == 5
    
    

