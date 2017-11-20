import random

class BingoCage:
    def __init__(self, items):
        self._items = list(items) #ローカルコピーで副作用を防止
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    
    def __call__(self):
        return self.pick()

if __name__ == '__main__':
    bingo = BingoCage(range(3))
    print('callable(bingo): ', callable(bingo))
    print('bingo.pick(): ', bingo.pick())
    print('bingo(): ', bingo())
    print('bingo(): ', bingo())
    # LookupError: pick from empty BingoCage
    #print('bingo(): ', bingo())