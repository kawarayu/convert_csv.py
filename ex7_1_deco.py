def deco(func):
    def inner():
        print('running inner()')
    return inner    # funcは使用しない

@deco
def target():
    print('running target()')

def main():
    print(target())
    print(target)

if __name__ == '__main__':
    main()