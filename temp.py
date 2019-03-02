def f():
    y=3
    yield 4
    print('哈哈')
a=f()
print(next(a),a)