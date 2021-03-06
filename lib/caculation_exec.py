from lib.fetch_input import fetch_product_sum, fetch_is_prod_imported, fetch_prod_price, fetch_prod_name
from lib.vali_input import is_prod_tax_free, caculate_tax, round_nr

class TaxCaculator:
    '''
    A class for tax caculation

    Method
    -----
    tax_cacul_exec(str_input)
        caculate the price after tax
    '''

    def tax_cacul_exec(self, str_input):
        '''
        : param str_input: product info input
        :return: [original price of product, price after tax caculation]
        '''
        origin_price = fetch_prod_price(str_input)
        price_after_tax = caculate_tax(str_input)[0] 
        
        
        return [origin_price, round_nr(price_after_tax)]