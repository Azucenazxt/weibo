from models.weibo import Weibo
from models.user import User
from routes import *

main = Blueprint('weibo', __name__)


def valid_user(u, w, username):
    return u.username == username and w.user_w.username == u.username

@main.route('/<username>/timeline')
def index(username):
    u = current_user()
    weibos = Weibo.query.all()
    return render_template('timeline.html', weibos=weibos, user=u)


@main.route('/add', methods=['POST'])
@login_required
def add():
    u = current_user()
    form = request.form
    w = Weibo(form)
    w.user_id = u.id
    if w.valid():
        w.save()
    return redirect(url_for('.index', username=u.username))


@main.route('/<username>/delete/<int:weibo_id>')
def delete(username, weibo_id):
    u = current_user()
    if u is None:
        return redirect(url_for('user.index'))
    else:
        w = Weibo.query.get(weibo_id)
        if valid_user(u, w, username):
            for c in w.comments:
                c.delete()
            w.delete()
        return redirect(url_for('.index', username=username))


@main.route('/<username>/edit/<int:weibo_id>', methods=['POST'])
def edit(username, weibo_id):
    w = Weibo.query.get(weibo_id)
    u = current_user()
    if u is None:
        return redirect(url_for('user.index'))
    elif valid_user(u, w, username):
        new_content = request.form.get('new-content')
        if len(new_content) > 0:
            w.content = new_content
            w.save()
    return redirect(url_for('.index', username=u.username))




