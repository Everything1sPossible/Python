"""
配置表
"""
import os
# DEBUG模式
DEBUG = True
# 不设置该变量,使用session时报错,设置为24个字符的字符串
SECRET_KEY = os.urandom(24)

# 数据库配置,基于flask-SQLAlchemy
DIALECT = 'mysql'  # 方言
DRIVER = 'pymysql'  # 数据库驱动
USERNAME = 'root'  # 用户名
PASSWORD = '123456'  # 密码
HOST = '127.0.0.1'  # 主机
PORT = '3306'  # mysql端口
DATABASE = 'testdb'  # mysql数据库
# 基于以上配置定义SQLALCHEMY_DATABASE_URI
SQLALCHEMY_DATABASE_URI = '{0}+{1}://{2}:{3}@{4}:{5}/{6}?charset=utf8'.format(DIALECT, DRIVER, USERNAME,
                                                                              PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

