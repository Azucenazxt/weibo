from . import ModelMixin
from . import db
from . import timestamp


class Weibo(db.Model, ModelMixin):
    __tablename__ = 'weibos'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String())
    created_time = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='weibo')



    def __init__(self, form):
        self.content = form.get('content', '')
        self.username = form.get('username', '')
        self.created_time = timestamp()


    def valid(self):
        return len(self.content) > 0