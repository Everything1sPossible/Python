"""
工具函数表
"""
import functools
from flask import redirect, session, url_for, request
import hashlib


def login_required(url_fun, target_id_name=None):
    """
    检查是否登录装饰器
    :param url: 用于指定登录之后跳转的路径反转函数
    :param target_id_name: 如果传入该值,该值表示详情页面路径的id参数名称
            例如:http://127.0.0.1:5000/index/detail/c32df848-157e-11e8-a347-005056c00008
            target_id_name=article_id
    :return:
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if session.get('user_id'):
                return func(*args, **kw)
            else:
                if target_id_name:
                    request_url = request.path
                    detail_id = request_url.split("/")[-1]  # 此处用于详情页面取ID
                    from_url = url_fun+'|'+target_id_name+'|'+detail_id
                    return redirect(url_for('index.to_login', from_url_fun=from_url))
                else:
                    return redirect(url_for('index.to_login', from_url_fun=url_fun))
        return wrapper
    return decorator


def md5str(context):
    """
    对传入字符串进行md5加密
    :param context: 对象字符串
    :return:
    """
    md5 = hashlib.md5()
    md5.update(context.encode('utf-8'))
    return md5.hexdigest()


def interval(context, start=None, end=None):
    """
    对字符串进行截取操作(用于自定义jinja2模板过滤器,也可用于工具函数)
    :param context: 目标字符串
    :param start: 开始下标
    :param end: 结束下标
    :return:
    """
    if end is None:
        return context[int(start):]
    elif start is None:
        return context[:int(end)]
    return context[int(start):int(end)]






