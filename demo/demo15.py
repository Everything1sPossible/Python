"""
python3 面向对象
    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    实例变量：定义在方法中的变量，只作用于当前实例的类。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，
          有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
对象可以包含任意数量和类型的数据。
"""


class MyClass:
    """
    类对象支持两种操作：属性引用和实例化。
    属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。
    类对象创建后，类命名空间中所有的命名都是有效属性名
    """
    i = 12345

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass 类直接进行属性引用", MyClass.i)
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())


class MyClass2:
    """
    很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
    类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法
     __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上

    self代表类的实例，而非类
    类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self
    self 不是 python 关键字，我们把他换成 runoob(任一名称) 也是可以正常执行的
    """
    # 构造函数
    def __init__(self, r, s):
        self.r = r
        self.s = s

    def sel(self):
        print(self)
        print(self.__class__)

    def sel2(runoob):
        print(runoob)
        print(runoob.__class__)


x = MyClass2("jack", 21)
x.sel()
x.sel2()
print(x.r, x.s)


class people(object):
    """
    类的方法
    在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例
    """
    # 定义属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob',10,30)
p.speak()
"""
python3 继承
"""


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()


# 多继承实例
# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    """
        需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
        python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
    """
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法


"""
类属性与方法
1.类的私有属性
    __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
2.类的私有方法
    __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。
3.类的专有方法：
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
"""
