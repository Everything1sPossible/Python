"""
主文件
"""
from flask import Flask, render_template
from app.manager import db
import app.config
from app.article_management.views import index
from app.utils import interval

app = Flask(__name__)
# 装载配置文件
app.config.from_object(config)

# flask_sqlalchemy绑定app
db.init_app(app)

# 注册自定义过滤器
env = app.jinja_env
env.filters['interval'] = interval
# 注册蓝图
app.register_blueprint(index, url_prefix='/index')


# 自定义错误模板
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500




