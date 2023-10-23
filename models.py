from typing import Optional
from sqlalchemy import DateTime, ForeignKey, Integer, String, Text
from init import db
from sqlalchemy.orm import Mapped, Relationship, mapped_column
from datetime import datetime


DEFAULT_IMG = "https://wallpapercave.com/wp/wp12696574.jpg"
   

class Post(db.Model):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, nullable=False, default=datetime.today())
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False)

    hashtag: Mapped[Relationship] = Relationship('PostTag', backref='post')

    def __init__(self, **kwargs) -> None:
        super(Post, self).__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Post: {self.title}>"


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=False)
    image_url: Mapped[Optional[str]] = mapped_column(String, default=DEFAULT_IMG)

    posts: Mapped[Post] = Relationship("Post", backref="user", cascade="all, delete")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __init__(self, **kwargs) -> None:
        super(User, self).__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<User: {self.full_name}>"


class Tag(db.Model):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    posts: Mapped[Relationship] = Relationship('PostTag', backref='tag')


class PostTag(db.Model):
    __tablename__ = 'post_tags'

    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('posts.id'), primary_key=True)
    tag_id: Mapped[int] = mapped_column(Integer, ForeignKey('tags.id'), primary_key=True)


