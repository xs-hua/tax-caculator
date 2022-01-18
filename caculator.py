
from lib.caculation_exec import TaxCaculator
from lib.fetch_input import fetch_prod_name, fetch_prod_price, fetch_product_sum
from lib.vali_input import caculate_tax, round_nr


if __name__ == "__main__":

    origin_price = 0.0
    price_sum = 0.0
    prod_list = []

    running = True

    executor = TaxCaculator()

    while(running):
        print("> ", end="")
        input_str = input()
        input_str = input_str.strip()

        if not input_str:
            break
        elif len(input_str.split(" ")) < 3:
            continue
        else:
            prod_list.append([fetch_product_sum(input_str), fetch_prod_name(input_str), round_nr(caculate_tax(input_str)[0])])
            result = executor.tax_cacul_exec(input_str)
            origin_price += result[0]
            price_sum += round(result[1], 2)

    for p in prod_list:
        print("> {} {}: {}".format(p[0], p[1], p[2]))    
        
    print("> Sales Taxes: {}".format(round(price_sum - origin_price, 2)))
    print("> Total: {}".format(round(price_sum, 2)))


