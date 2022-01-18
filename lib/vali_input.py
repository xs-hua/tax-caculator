

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

    return [round(price*add_tax, 3), round(price*add_tax-price, 3)]


    '''

    price_tax = round(price*add_tax, 2)
    price_tax_str = str(int(price_tax*100))
    
    #round price number to 0.05
    if int(price_tax_str[-1]) < 5:
        price_tax_str = list(price_tax_str)
        price_tax_str[-1] = '5'
        price_tax = float("".join(price_tax_str)) / 100
        
    tax = price*add_tax - price
    tax_str = str(int(tax*100))

    print(tax)

    #round tax number to 0.05
    if tax != 0.0 and int(tax_str[-1]) != 0 and int(tax_str[-1]) < 5:
        tax_str = list(tax_str)
        tax_str[-1] = '5'
        tax = float("".join(tax_str)) / 100

    return [price_tax, tax]

    '''


    
    

