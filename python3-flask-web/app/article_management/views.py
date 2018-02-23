from flask import render_template, Blueprint, session, request, redirect, url_for
from app.manager import db
from app.utils import login_required, md5str, interval
from app.article_management.domain import UserLogin, Article, ArticleComment
from app.constants import PER_PAGE

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    context = {}
    page = request.args.get('page', 1, type=int)  # 页码
    search_code = request.form.get('search_code') if request.form.get('search_code') else request.args.get('search_code')
    # 模糊查询db.or_:or, db.and_:and
    if search_code:
        pagination = Article.query.filter(db.or_(Article.arTitle.ilike('%'+search_code+'%'),
                                          Article.arContent.ilike('%'+search_code+'%'))).\
            order_by(db.desc(Article.create_time)).paginate(page, per_page=PER_PAGE)
    else:
        pagination = Article.query.order_by(db.desc(Article.create_time)).paginate(page, per_page=PER_PAGE)
    result = pagination.items  # 获取分页对象中的查询结果
    context['articles'] = result
    context['pagination'] = pagination
    context['search_code'] = search_code
    return render_template('index.html', **context)


@index.route('/login', methods=['GET', 'POST'])
def to_login():
    if request.method == 'GET':
        # 此处将目标路径反转函数传到模板
        return render_template('login.html', from_url_fun=request.args.get('from_url_fun'))
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember')
        from_url_fun = request.form.get('from_url_fun')  # 目标路径反转函数
        userlogin = UserLogin.query.filter(UserLogin.username == username, UserLogin.password == md5str(password)).first()
        if userlogin:
            session["user_id"] = userlogin.id + userlogin.username
            if remember == '1':
                session.permanent = True
            if from_url_fun is not None and from_url_fun != 'None':
                if from_url_fun.find('|') == -1:
                    return redirect(url_for('index.' + from_url_fun))
                else:
                    from_url_list = from_url_fun.split('|')
                    target_id_name = from_url_list[1]
                    values = {
                        target_id_name: from_url_list[2]
                    }
                    return redirect(url_for('index.'+from_url_list[0], **values))
            else:
                return redirect(url_for('index.home'))
        else:
            context = {
                "message": "用户名或密码错误!",
                "username": username
            }
            return render_template('login.html', **context)


@index.route('/regist', methods=['GET', 'POST'])
def to_regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        context = {}
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        context['username'] = username
        if password1 != password2:
            context['message'] = "两次密码输入不一致!"
            return render_template('regist.html', **context)
        else:
            new_user_login = UserLogin(username=username, password=md5str(password1))
            try:
                db.session.add(new_user_login)
                db.session.commit()
                return redirect(url_for('index.to_login'))
            except:
                db.session.rollback()
                context['message'] = "注册失败!!"
                return render_template('regist.html', **context)


@index.route('/login_out', methods=['GET', 'POST'])
def login_out():
    session.pop('user_id', None)
    return redirect(url_for('index.home'))


@index.route('/to_add_article', methods=['GET', 'POST'])
@login_required('to_add_article')
def to_add_article():
    if request.method == 'GET':
        return render_template('article_management/article.html')
    else:
        context = {}
        arTitle = request.form.get('arTitle')
        arContent = request.form.get('arContent')
        authorId = interval(session.get('user_id'), end=36)
        new_article = Article(arTitle=arTitle, arContent=arContent, authorId=authorId)
        context['arTitle'] = arTitle
        context['arContent'] = arContent
        try:
            db.session.add(new_article)
            db.session.commit()
            context['message'] = '发布成功!'
        except:
            db.session.rollback()
            context['message'] = '发布失败!'
        return render_template('article_management/article.html', **context)


@index.route('/detail/<article_id>', methods=['GET', 'POST'])
# @login_required('to_article_detail', target_id_name='article_id')
def to_article_detail(article_id):
    context = {}
    page = request.args.get('page', 1, type=int)  # 页码
    article_detail = Article.query.get(article_id)
    pagination = ArticleComment.query.filter(ArticleComment.articleId == article_id).\
        order_by(db.desc(ArticleComment.create_time)).paginate(page, per_page=PER_PAGE)
    result = pagination.items  # 获取分页对象中的查询结果
    context['article_detail'] = article_detail
    context['comments'] = result
    context['pagination'] = pagination
    return render_template('article_management/article_detail.html', **context)


@index.route('/comment/<article_id>', methods=['POST'])
@login_required('to_article_detail', target_id_name='article_id')
def to_add_comment(article_id):
    authorId = interval(session.get('user_id'), end=36)
    acContent = request.form.get('acContent')
    new_article_comment = ArticleComment(acContent=acContent, articleId=article_id, authorId=authorId)
    try:
        db.session.add(new_article_comment)
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('index.to_article_detail', article_id=article_id))



