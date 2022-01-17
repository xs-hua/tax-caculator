# tax-caculator

## Prerequisite
1. Install Python3, pip3
2. Run `python3 -m venv YOUR-ENV-NAME`
3. Run `source YOUR-ENV-NAME/bin/activate`
4. Run `pip3 install -r requirements.txt`

## Feature
1. Fetch product sum, imported keyword, product name and product price
2. Tax is caculated as followings:
    - Basic tax on all product categories (exclu. books, food and medical products): 10%
    - Extra tax on imported products: 5%
3. Print total price of the inputted product (inclu. tax)

## How to run
1. Run app: `python3 app.py`
2. Run test: `pytest`