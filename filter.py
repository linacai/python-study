def _odd_iter():
    n = 1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x: x%n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

print(list(filter(_not_divisible(3),range(1,20))))

def is_palindrome(n):
    if str(n)==str(n)[::-1]:
       return n

print(list(filter(is_palindrome,range(1,30))))

def by_name(s):
    return s[0]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L,key=by_name))

def by_score(t):
    return t[1]
print(sorted(L,key=by_score))

import functools
def log(text=None):
    def decrator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('begin call %s():' % func.__name__)
            result=func(*args,**kw)
            print('end call %s():' % func.__name__)
            if text !=None:
               print('%s' % text)
            return result
        return wrapper
    return decrator

@log()
def now():
    print('16:00')

@log('excute')
def new():
    print('who cares')

now()
new()
