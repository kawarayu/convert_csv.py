import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = [f'{k}={w}' for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
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