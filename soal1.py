def generate100():
    return [i for i in range(100, 0, -1)]

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def foo_bar(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FooBar'
    elif n % 3 == 0:
        return 'Foo'
    elif n % 5 == 0:
        return 'Bar'
    else:
        return n

def run():
    ints = generate100()
    for n in ints:
        if is_prime(n):
            continue
        else:
            print(foo_bar(n), end=', ')

run()