from models.user import User
from routes import *


main = Blueprint('user', __name__)

Model = User

@main.route('/')
def login_index(msgs=''):
    return render_template('user_login.html', msgs=msgs)


@main.route('/register')
def register_index(msgs=''):
    return render_template('user_register.html', msgs=msgs)


@main.route('/user/register', methods=['POST'])
def register():
    form = request.form
    m = Model(form)
    message = m.valid_register()
    if message[0]:
        if m.avatar == '':
            m.avatar = 'http://ww4.sinaimg.cn/mw690/a5047993jw1f8ugjis83tg202s02sgli.gif'
        if m.title == '':
            m.title = ''
        m.save()
    msgs = message[1]
    return render_template('user_login.html', msgs=msgs)


@main.route('/user/login', methods=['POST'])
def login():
    form = request.form
    m = Model(form)
    message = m.valid_login()
    if message[0]:
        return redirect(url_for('weibo.index', username=m.username))
    else:
        msgs = message[1]
    return render_template('user_login.html', msgs=msgs)


@main.route('/user/profile/<int:id>')
def profile(id):
    m = Model.query.get(id)
    return render_template('profile.html', user=m)


@main.route('/user/title', methods=['POST'])
def change():
    id = request.form.get('user_id')
    m = Model.query.get(id)
    m.title = request.form.get('title')
    m.save()
    return redirect(url_for('weibo.index', username=m.username))

