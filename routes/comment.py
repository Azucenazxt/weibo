from models.comment import Comment
from routes import *


main = Blueprint('comment', __name__)

Model = Comment

@main.route('/comment', methods=['POST'])
def add():
    u = current_user()
    if u is None:
        return redirect(url_for('user.index'))
    form = request.form
    c = Comment(form)
    c.user_id = u.id
    c.weibo_id = int(form.get('weibo_id'))
    # if c.valid_comment():
    c.save()
    return redirect(url_for('weibo.index', username=u.username))


