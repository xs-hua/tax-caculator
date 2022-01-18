import pytest

from lib.vali_input import is_prod_tax_free

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




class TestInputValidation:

    #test validate prod name
    def test_valid_prod_tax_free(self, prod_names):
        for name in prod_names:
            assert is_prod_tax_free(name[0]) == name[1]
     
            

        