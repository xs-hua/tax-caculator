import pytest

from lib.vali_input import is_prod_tax_free, caculate_tax

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
    prod_list.append(["1 book at 12.49", 12.49, 0.0])
    prod_list.append(["1 imported box of chocolates at 10.00", 10.5, 0.5])
    prod_list.append(["1 imported bottle of perfume at 47.50", 54.625, 7.125 ])

    return prod_list


class TestInputValidation:

    #test validate prod name
    def test_valid_prod_tax_free(self, prod_names):
        for name in prod_names:
            assert is_prod_tax_free(name[0]) == name[1]
     
    def test_tax_caculation(self, prod_taxes):
        for p in prod_taxes:
            assert caculate_tax(p[0])[0] == p[1]
            assert caculate_tax(p[0])[1] == p[2]
        