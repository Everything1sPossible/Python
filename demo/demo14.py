"""
Python有两种错误很容易辨认：语法错误和异常。
      Python 的语法错误或者称之为解析错
      运行期检测到的错误被称为异常
"""
import sys

try:
    """
    try语句按照如下方式工作；
        首先，执行try子句（在关键字try和关键字except之间的语句）
        如果没有异常发生，忽略except子句，try子句执行后结束。
        如果在执行try子句的过程中发生了异常，那么try子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的except子句将被执行。
        最后执行 try 语句之后的代码。
        如果一个异常没有与任何的except匹配，那么这个异常将会传递给上层的try中。
    """
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
except:
    """
    最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
    """
    print("Unexpected error:", sys.exc_info()[0])
    # 将异常抛出
    raise
finally:
    print("finally....")


# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except (ValueError) as Argument:
        print ("参数没有包含数字\n", Argument)


# 调用函数
temp_convert("xyz")

