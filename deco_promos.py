promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order): 
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """7% discount for orders with 10 or more distinct items""" 
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    return max(promo(order) for promo in promos)

if __name__ == '__main__':
    from ex6_2_strategy_order_functional import Customer, LineItem, Order
    joe = Customer('Joh Doe', 0)
    ann = Customer('Ann Smith', 1100)
    normal_cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0)]

    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apole', 10, 1.5)]

    long_order = [LineItem(str(item_code), 1, 1.0)
                 for item_code in range(10)]

    carts = [normal_cart, banana_cart, long_order]
    for who in [joe, ann]:
        for cart in carts:
            print(Order(who, cart, best_promo))