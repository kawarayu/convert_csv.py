import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print(f'[{elapsed:0.8f}] {name}({arg_str}) -> {result}')
        return result
    return clocked

def main():
    @clock
    def snooze(seconds):
        time.sleep(seconds)
    
    @clock
    def factorial(n):
        return 1 if n < 2 else n * factorial(n-1)
    
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factrial(6)')
    print('6! =', factorial(6))

if __name__ == '__main__':
    main()