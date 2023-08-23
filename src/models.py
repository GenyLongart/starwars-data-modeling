import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False)
    posts = relationship('Post', backref="user")
    comments = relationship('Comment', backref="user")

class Planet(Base):
    __tablename__ = 'planets'
    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
