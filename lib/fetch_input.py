
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

def fetch_prod_price(str):
    str_arr = str.split(" ")

    try:
        price = float(str_arr[len(str_arr) - 1])
    except ValueError as e:
        print(e)
    
    return price

def fetch_prod_name(str):
    str_arr = str.split(" ")
    
    try:
        if len(str_arr) == 4:
            name = str_arr[1]
        else:
            match_result = re.search( r'(\w+) (.*) (.+) at (.+)', str, re.I)      
            name = match_result.group(3)

            words_before_name = match_result.group(2).split(" ")[-1]         
            #check if product name contains two words
            if words_before_name != "of" and words_before_name != "imported":
                name = words_before_name+" "+name

        return name;        
    except Exception as e:
        print(e)









