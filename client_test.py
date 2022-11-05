from random import random

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    """ ------------- Update this function ------------- """
    try:
        return price_a / price_b
    except ZeroDivisionError:
        return

if __name__ == "__main__":
    price_a = round(10 * random())
    b_lst = [round(10 * random()), 0]
    print(price_a, b_lst[0])
    print(getRatio(price_a, b_lst[0]))
    print(getRatio(price_a, b_lst[1]))
