from app import db, login
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(64), index=True, unique=True)
    password: Mapped[str] = mapped_column(db.String(128))
    remember: Mapped[bool] = mapped_column(db.Boolean, default=False)
    last_login: Mapped[datetime] = mapped_column(db.DateTime)
    profile_pic: Mapped[str] = mapped_column(db.String(256), nullable=True)
    bio: Mapped[str] = mapped_column(db.Text, nullable=True)
    posts: Mapped[list['Post']] = relationship(back_populates='author')

    def __repr__(self):
        return f'<User {self.username}>'

@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    body: Mapped[str] = mapped_column(db.Text)
    timestamp: Mapped[datetime] = mapped_column(db.DateTime, index=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    author: Mapped['User'] = relationship(back_populates='posts')

    def __repr__(self):
        return f'<Post {self.body[:20]}>'