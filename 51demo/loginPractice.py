def login(username, password):
    """
    登录函数
    :param username:用户名
    :param password: 密码
    :return:
    """
    file = open("db", "r")
    for line in file:
        up_list = line.strip('\r\n').split("|")
        print(up_list)
        if up_list[0] == username and up_list[1] == password:
            return True
    return False


def register(username, password):
    """
    注册函数
    :param username:用户名
    :param password: 密码
    :return:
    """
    file = open("db", "a")
    try:
        file.write(username + "|" + password + "\r\n")
        file.close()
        return True
    except Exception:
        return False


def main():
    """
    主函数
    :return:
    """
    while True:
        choose = input("请选择(1:登录,2:注册):")
        if choose == "1":
            username = input("输入用户名:")
            password = input("输入密码:")
            result = login(username, password)
            if result:
                print("登录成功!")
                break
            else:
                print("账号或密码错误!")
        elif choose == "2":
            username = input("输入用户名:")
            password = input("输入密码:")
            result = register(username, password)
            if result:
                print("注册成功!")
                break
            else:
                print("注册失败!")


main()

