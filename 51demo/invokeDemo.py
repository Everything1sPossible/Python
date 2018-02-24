# import test.commons


def import_demo():
    # fromlist=True表示按照连接的方式查找,如果不设置该参数,默认之后查找test/__init__.py
    commons = __import__('test.commons', fromlist=True)
    print(commons)


def run():
    commons = __import__('commons')  # 动态导入模块(此处是写死的)
    inp = input('请输入::')
    if hasattr(commons, inp):  # 判断成员是否存在
        func = getattr(commons, inp)  # 获取函数
        func()  # 输出::登录..
        setattr(commons, inp, lambda: print('反射后..'))  # 修改函数体
        func_after = getattr(commons, inp)  # 重新获取函数
        func_after()  # 输出::反射后..
    else:
        print('404')


if __name__ == '__main__':
    import_demo()