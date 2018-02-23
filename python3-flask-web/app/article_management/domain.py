from app.manager import db
from uuid import uuid1
from numpy import unicode
import datetime

"""
文章管理实体类
"""


# 用户登录类
class UserLogin(db.Model):

    __tablename__ = 'user_login'
    id = db.Column(db.String(36), default=lambda: unicode(uuid1()), primary_key=True)  # 主键
    username = db.Column(db.String(50), nullable=False)  # 用户名
    password = db.Column(db.String(50), nullable=False)  # 密码
    create_time = db.Column(db.String(40), default=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 注册时间
    pwd_update_time = db.Column(db.String(40))  # 密码修改时间


# 用户信息类(暂未用到)
class UserInfo(db.Model):

    __tablename__ = 'user_info'

    id = db.Column(db.String(36), default=lambda: unicode(uuid1()), primary_key=True)  # 主键
    peName = db.Column(db.String(20), nullable=False)  # 姓名
    peNum = db.Column(db.String(20), nullable=False)  # 身份证
    peSex = db.Column(db.String(1), nullable=False)  # 性别
    peAge = db.Column(db.String(3), nullable=False)  # 年龄


# 文章类
class Article(db.Model):

    __tablename__ = 'article'

    id = db.Column(db.String(36), default=lambda: unicode(uuid1()), primary_key=True)  # 主键
    arTitle = db.Column(db.String(100), nullable=False)  # 标题
    arContent = db.Column(db.Text, nullable=False)  # 内容
    create_time = db.Column(db.String(40),
                            default=lambda: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 发布时间
    authorId = db.Column(db.String(36), db.ForeignKey('user_login.id'))  # 关联用户id

    author = db.relationship('UserLogin', backref=db.backref('articles', lazy='dynamic'))


class ArticleComment(db.Model):

    __tablename__ = 'article_comment'

    id = db.Column(db.String(36), default=lambda: unicode(uuid1()), primary_key=True)  # 主键
    acContent = db.Column(db.Text, nullable=False)  # 评论内容
    create_time = db.Column(db.String(40),
                            default=lambda: datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))  # 评论时间
    articleId = db.Column(db.String(36), db.ForeignKey('article.id'))  # 关联文章id
    # article = db.relationship('Article', backref=db.backref('comments', lazy='joined'))

    authorId = db.Column(db.String(36), db.ForeignKey('user_login.id'))  # 关联用户id
    author = db.relationship('UserLogin', backref=db.backref('comments', lazy='dynamic'))
