

from lib.fetch_input import fetch_is_prod_imported, fetch_prod_name, fetch_prod_price

TAX_FREE_CATE = ["book", "books", 
    "chocolate", "chocolates", 
    "pill", "pills"]

def is_prod_tax_free(prod_name):
    is_prod_tax_free = False

    prod_name_list = prod_name.split(" ")

    #check if any name keyword in tax free category
    for name in prod_name_list:
        if name in TAX_FREE_CATE:
            is_prod_tax_free = True
    
    return is_prod_tax_free


def caculate_tax(input_str):
    add_tax = 1
    price = fetch_prod_price(input_str)
    #tax = 0

    if fetch_is_prod_imported(input_str):
        add_tax = add_tax + 0.05
    
    if is_prod_tax_free(fetch_prod_name(input_str)) == False:
        add_tax = add_tax + 0.1

    return [round(price*add_tax, 2), round(price*add_tax-price, 2)]

def round_nr(nr):
    nr_str = str(int(nr*100))
    last_nr = nr_str[-1]

    #round number to 0.05
    if int(last_nr) != 0 and int(last_nr) < 5:
        nr_str = list(nr_str)
        nr_str[-1] = '5'
        nr = float("".join(nr_str)) / 100
    
    return nr

    
    

