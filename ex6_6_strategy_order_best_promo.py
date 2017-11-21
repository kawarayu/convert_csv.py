# ex6-6 関数のリストを反復処理
from ex6_2_strategy_order_functional import fidelity_promo, bulk_item_promo, large_order_promo

promos = [fidelity_promo, bulk_item_promo, large_order_promo]

def best_promo(order):
    return max(promo(order) for promo in promos)


# ex6-7 モジュールのグローバル名前空間をイントロスペクションする
promos2 = [globals()[name] for name in globals()
            if name.endswith('_promo')
            and name != 'best_promo']

def best_promo2(order):
    return max(promo(order) for promo in promos2)


# ex6-8 新しく用意したpromotionsモジュールをイントロスペクションする
import inspect
import promotions

promos3 = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]

def best_promo3(order):
    return max(promo(order) for promo in promos3)

if __name__ == '__main__':
    from ex6_2_strategy_order_functional import Customer, LineItem, Order
    joe = Customer('Joh Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, .5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0)]

    print(Order(joe, cart, fidelity_promo))
    print(Order(ann, cart, fidelity_promo))

    banana_cart = [LineItem('banana', 30, .5),
                   LineItem('apole', 10, 1.5)]
    print(Order(joe, banana_cart, bulk_item_promo))

    long_order = [LineItem(str(item_code), 1, 1.0)
                 for item_code in range(10)]
    print(Order(joe, long_order, large_order_promo))
    print(Order(joe, cart, large_order_promo))

 
    print(Order(joe, long_order, best_promo))
    print(Order(joe, long_order, best_promo2))
    print(Order(joe, long_order, best_promo3))
    
    print(Order(ann, long_order, best_promo))
    print(Order(ann, long_order, best_promo2))
    print(Order(ann, long_order, best_promo3))
