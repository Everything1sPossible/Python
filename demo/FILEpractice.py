import os
"""
os 模块提供了非常丰富的方法用来处理文件和目录
"""
ls = []


def getAppointFile(path, ls):
    filelist = os.listdir(path)
    try:
        for tmp in filelist:
            pathTmp = os.path.join(path, tmp)
            if os.path.isdir(pathTmp):
                getAppointFile(pathTmp, ls)
            elif pathTmp[pathTmp.rfind('.')+1:].upper() == 'PY':
                ls.append(pathTmp)
    except PermissionError:
        print("程序出错!!")


def main():
    while True:
        path = input('请输入路径:').strip()
        if os.path.isdir(path):
            print("程序执行中,请稍后!")
            break
        else:
            print("请输入正确的路径!")
    getAppointFile(path, ls)
    print(len(ls))
    print(ls)
    for f in ls:
        print(f)


main()
