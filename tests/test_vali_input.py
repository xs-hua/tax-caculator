import pytest

from lib.vali_input import is_prod_tax_free, caculate_tax, round_nr
from lib.fetch_input import fetch_prod_price
from lib.caculation_exec import TaxCaculator

#normal prod name
@pytest.fixture
def prod_names():
    prod_list = []

    prod_list.append(["book", True])
    prod_list.append(["books", True])
    prod_list.append(["chocolate", True ])
    prod_list.append(["chocolates", True])
    prod_list.append(["chocolate bar", True])
    prod_list.append(["metall bar", False])

    return prod_list

#prod with tax
@pytest.fixture
def prod_taxes():
    prod_list = []
    prod_list.append(["1 imported box of chocolates at 10.00", 10.5, 0.5])
    prod_list.append(["1 imported bottle of perfume at 47.50", 54.63, 7.13])

    return prod_list

#data for testing nr rounding to 0.05
@pytest.fixture
def unrounded_nrs():
    return [[6.10, 6.10], [6.12, 6.15], [6.18, 6.18]]

#prod with tax
@pytest.fixture
def prods():
    prod_list = []
    prod_list.append(
        [
        ["1 book at 12.49", "1 music CD at 14.99", "1 chocolate bar at 0.85"], 
        29.83,
        1.5
        ])
    prod_list.append(
        [
        ["1 imported box of chocolates at 10.00", "1 imported bottle of perfume at 47.50"], 
        65.15,
        7.65
        ])
    prod_list.append(
        [
        ["1 imported bottle of perfume at 27.99", "1 bottle of perfume at 18.99", "1 packet of headache pills at 9.75", "1 box of imported chocolates at 11.25"], 
        74.68,
        6.7
        ])
    
    return prod_list

class TestInputValidation:

    #test validate prod name
    @pytest.mark.validate_info
    def test_valid_prod_tax_free(self, prod_names):
        for name in prod_names:
            assert is_prod_tax_free(name[0]) == name[1]

    @pytest.mark.validate_info
    def test_tax_cacul(self, prod_taxes):
        for p in prod_taxes:
            result = caculate_tax(p[0])
            assert result[0] == p[1]
            assert result[1] == p[2]
    
    @pytest.mark.validate_info
    def test_round_nr(self, unrounded_nrs):
        for nr in unrounded_nrs:
            assert round_nr(nr[0]) == nr[1]

    @pytest.mark.validate_info 
    def test_tax_cacul_and_round_nr(self, prods):

        for p in prods:
            origin_price = 0.0
            price_sum = 0.0
            
            for item in p[0]:
                origin_price += fetch_prod_price(item)
                result = caculate_tax(item)
                price_sum += round_nr(result[0])
                
            assert round(price_sum, 2) == p[1]
            assert round(price_sum - origin_price, 2) == p[2]

    @pytest.mark.validate_info     
    def test_excutor(self):
        executor = TaxCaculator()
        result = executor.tax_cacul_exec("1 book at 12.49")
        assert result[0] == 12.49
        assert result[1] == 12.49

        result = executor.tax_cacul_exec("1 imported box of chocolates at 10.00")
        assert result[0] == 10.0
        assert result[1] == 10.5