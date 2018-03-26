"""
Super advanced ERP
"""

apple_stock = [1, 2, 3]
employee_count = 7

from package import sum

#def compute_benefits(apple_count):
#    print("That'll be {} apples per employee".format(divide(apple_count, employee_count)))

def account_stock(stock, product):
    print("{} {}!".format(sum(stock), product))

def main():
    account_stock(apple_stock, "apples")

if __name__ == "__main__":
    main()
