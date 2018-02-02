"""
装饰器demo
"""
import functools
import time
import datetime


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        # 增强内容
        print('call %s():' % func.__name__)
        # 执行原函数
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()
"""
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
"""


def log1(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log1('execute')
def now1():
    print('2015-3-25')


now1()
print(now1.__name__)
"""
请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
"""


def metric(text):
    def decorator(func):
        starttime = time.clock()

        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            fun = func(*args, **kw)
            endtime = time.clock()
            # d1 = datetime.datetime.
            print("执行时间: %s" % (endtime - starttime))
            return fun
        return wrapper
    return decorator


@metric("do")
def fast(x, y):
    time.sleep(5)
    return x + y;


print(fast(1, 2))

