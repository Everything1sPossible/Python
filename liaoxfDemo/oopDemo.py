from types import MethodType


def set_age(self, age):
    self.age = age


class Student(object):
    """
    为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性.
    使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
    """
    # __slots__ = ('name', 'age')

    @property
    def score(self):
        return self.score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.score = value


# 实例化Student
s = Student()
# 给s绑定set_age函数
# s.set_age = MethodType(set_age, s)
# s.set_age(20)
# print(s.age)
# s.score = 69
# print(s.score)


class str_demo(object):
    def __init__(self, value):
        self.value = value

    """
    类似于java的toString方法
    """
    def __str__(self):
        return 'str_demo (value: %s)' % (self.value)


st = str_demo('您好!')
print(st)


class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
                return a
        # 如果是切片对象
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
        return L


f = Fib()
print(f[:10])
