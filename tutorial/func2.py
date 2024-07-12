# ----  匿名函数 -----
def hello(callback):
    callback("1122")


hello(lambda x: print(x))


# -------------装饰器-------------------
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def echo(name):
    print(name)


echo("111")


# ----------  生成器------------
def gen():
    n = 0
    while True:
        print("gen before yield:" + str(n))
        yield n
        print("gen after yield:" + str(n))
        n = n + 1


print(type(gen()))
g = gen()  # 函数gen()没有实际执行，只是返回一个生成器
print("before next")
m = g.__next__()  # 调用生成器的next 方法将触发gen() 函数执行，直到yield指令停止
print("after next")
print(m)
print("before next2")
m = g.__next__()  # 从上次停止的地方继续开始执行，直到yield指令
print("after next2")
print(m)


# before next
# gen before yield:0
# after next
# 0
# before next2
# gen after yield:0
# gen before yield:1
# after next2
# 1


def consumer():
    print("consumer start....")
    r = None
    while True:
        n = yield r
        if not n:
            return
        print("consumer.........." + str(n))
        r = n * n


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print("produce..........." + str(n))
        r = c.send(n)
        print(r)


produce(consumer())
