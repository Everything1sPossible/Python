import pymysql


def fetchone():
    """
    单条数据查询
    :return:
    """
    # 建立连接
    db = pymysql.connect("localhost", "root", "123456", "testdb")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("SELECT * from EMPLOYEE")
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print("Data : {0} ".format(data))
    # 关闭连接
    db.close()


def fetchall():
    """
    全部数据查询
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
    :return:
    """
    # 打开数据库连接
    db = pymysql.connect("localhost", "root", "123456", "TESTDB")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = "SELECT * FROM EMPLOYEE \
           WHERE INCOME > %s" % (1000)
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        # # 获取数据数量
        # count = cursor.rowcount
        # print(count)
        for row in results:
            fname = row[1]
            lname = row[2]
            age = row[3]
            sex = row[4]
            income = row[5]
            # 打印结果
            print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
                  (fname, lname, age, sex, income))
    except:
        print("Error: unable to fetch data")
    # 关闭数据库连接
    finally:
        if db:
            db.close()


def add():
    """
    数据库插入操作
    """
    # 打开数据库连接
    db1 = pymysql.connect("localhost", "root", "123456", "TESTDB")
    # 使用cursor()方法获取操作游标
    cursor1 = db1.cursor()
    # SQL 插入语句
    sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
             LAST_NAME, AGE, SEX, INCOME)
             VALUES ('Mac', 'Mohan', 20, 'M', 15000)"""
    """
    # 也可以换成下面这种写法
    # SQL 插入语句
    sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
           LAST_NAME, AGE, SEX, INCOME) \
           VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
          ('Mac', 'Mohan', 20, 'M', 2000)
    
    更新和删除操作只需要更改sql语句即可
    """
    try:
        # 执行sql语句
        cursor1.execute(sql)
        # 提交到数据库执行
        db1.commit()
    except:
        # 如果发生错误则回滚
        db1.rollback()
    # 关闭数据库连接
    finally:
        if db1:
            db1.close()


# fetchone()
# add()
fetchall()