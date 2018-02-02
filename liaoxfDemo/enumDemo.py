from enum import Enum, unique


Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


@unique  # @unique装饰器可以帮助我们检查保证没有重复值
class Weeekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


for name, member in Weeekday.__members__.items():
    print(name, '=>', member, ',', member.value)

