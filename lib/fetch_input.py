
def fetch_product_sum(str):
    try:
        global sum
        sum = int(str.split(" ")[0])
    except ValueError as e:
        print(e)
    
    return sum

