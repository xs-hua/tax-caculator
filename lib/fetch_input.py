
import re

def fetch_product_sum(str):
    try:
        global sum
        sum = int(str.split(" ")[0])
    except ValueError as e:
        print(e)
    
    return sum

def fetch_is_prod_imported(str):
    is_imported = False
    check_result = re.search('imported', str)

    if check_result != None:
        is_imported = True
    
    return is_imported




