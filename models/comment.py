from . import ModelMixin
from . import db
from . import timestamp


class Comment(db.Model, ModelMixin):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    weibo_id = db.Column(db.Integer, db.ForeignKey('weibos.id'))
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)


    def __init__(self, form):
        self.username = form.get('username', '')
        self.weibo_id = form.get('weibo_id', '')
        self.user_id = form.get('user_id', '')
        self.content = form.get('comment', '')
        self.created_time = timestamp()

    def valid_comment(self):
        return len(self.content) > 0