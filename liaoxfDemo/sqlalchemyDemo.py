from sqlalchemy import Column, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
# import pymysql

# 创建对象的基类
Base = declarative_base()


# 定义user对象
class User(declarative_base()):
    # 对象对应的表名
    __tablename__ = "user"

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(10), nullable=False)

    def __str__(self):
        return 'id: %s, name: %s' % (self.id, self.name)  # 此处必须有return


# 初始化数据库连接:
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/testdb')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# # 创建session对象
# session = DBSession()
# # 创建新user对象
# new_user = User(id='3', name='lulu')
# # 添加到session
# session.add(new_user)
# # 提交保存到数据库
# session.commit()
# # 关闭session
# session.close()

# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# user = session.query(User).filter(User.id=='1').one()
users = session.query(User).all()
# 打印类型和对象的name属性:
print('type:', type(users))
for i in users:
    print(i)
# 关闭Session:
session.close()
"""
===============================================================================================
"""
"""
一对多示例:
"""


class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')


class Book(Base):
    __tablename__ = 'book'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))