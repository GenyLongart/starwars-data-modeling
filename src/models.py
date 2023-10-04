import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Favorites_user_characters(Base):
    __tablename__ = 'favorites_user_characters'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class Favorites_user_planets(Base):
    __tablename__ = 'favorites_user_planets'
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=True)
    email = Column(String(100), nullable=False)
    characters = relationship('Character', backref="user")
    planets = relationship('Planet', backref="user")
    posts = relationship('Post', backref="user")

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name =  Column(String(100), nullable=False)
    population = Column(Integer, nullable=True)
    climate = Column(String(100), nullable=True)
    diameter = Column(Integer, nullable=True)
    favorite = Column(Boolean(), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    birth_year = Column(Integer, nullable=True)
    gender = Column(Integer, nullable=False)
    height = Column(Float, nullable=True)
    favorite = Column(Boolean(), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
