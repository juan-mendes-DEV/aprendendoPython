def func():
    print('function starts')
    yield
    print('end of function')

try:
    y = func()
    print(type(y))
    next(y)
    next(y)

except StopIteration as e:
    pass