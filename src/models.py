import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    followers = Column(Integer, nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    post = relationship("post")

class post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    media = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)
    comments = Column(Integer, nullable=False)
    caption = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)

class reels(Base):
    __tablename__ = 'reels'
    id = Column(Integer, primary_key=True)
    media = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)

class history(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    content = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('user.id'))
    post = relationship(user)

class chat(Base):
    __tablename__ = 'chat'
    id = Column(Integer, primary_key=True)
    message = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(user)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
