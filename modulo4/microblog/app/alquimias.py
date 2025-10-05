from datetime import datetime
from sqlalchemy import select
from app import db
from app.models.models import User, Post

def validate_user_password(username, password):
    res = db.session.scalars(select(User).where(User.username == username))
    user = res.first()
    if user and user.password == password:
        return user
    return None

def user_exists(username):
    res = db.session.scalars(select(User).where(User.username == username))
    return res.first()

def create_user(username, password, remember=False, last_login=None, profile_pic=None, bio=None):
    new_user = User(
        username=username,
        password=password,
        remember=remember,
        last_login=last_login if last_login else datetime.now(),
        profile_pic=profile_pic,
        bio=bio
    )
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_post(body, user):
    post = Post(
        body=body,
        timestamp=datetime.now(),
        user_id=user.id
    )
    db.session.add(post)
    db.session.commit()
    return post

def get_timeline():
    return db.session.scalars(select(Post).order_by(Post.timestamp.desc()).limit(5)).all()