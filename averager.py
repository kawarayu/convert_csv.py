from pprint import pprint as p

class Averager():
    
    def __init__(self):
        self.series = []
    
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series) # 毎回sumが走る
        return total/len(series) # 毎回lenが走る

    return averager

def make_averager_nonlocal():
    count, total = 0, 0
    
    def averager(new_value):
        nonlocal count, total
        count += 1 # lenとsum相当が記録される
        total += new_value
        return total / count

    return averager

def main():
    avg = make_averager_nonlocal()
    p(avg(10))
    p(avg(11))
    p(avg(12))


if __name__ == '__main__':
    main()