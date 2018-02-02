"""
在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally,
写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭.
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的。
"""
from contextlib import contextmanager
from contextlib import closing
from urllib.request import urlopen


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' % self.name)


with Query('Bob') as q:
    q.query()


"""
@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，然后，with语句就可以正常地工作了
"""


class Query1(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q1 = Query1(name)
    yield q1
    print('End')


with create_query('Bob') as q1:
    q1.query()

"""
代码的执行顺序是：
    1.with语句首先执行yield之前的语句，因此打印出<h1>；
    2.yield调用会执行with语句内部的所有语句，因此打印出hello和world；
    3.最后执行yield之后的语句，打印出</h1>。
    因此，@contextmanager让我们通过编写generator来简化上下文管理
"""


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

"""
如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
例如，用with语句使用urlopen()
closing也是一个经过@contextmanager装饰的generator

@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
"""
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)