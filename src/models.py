import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    # def to_dict(self):
    #     return {}

class User(Base):
    __tablename__ = "user"
    # Here we define columns for the table user
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(15), nullable=False)
    personajes_favoritos = relationship("Personajes_Favoritos")
    planetas_favoritos = relationship("Planetas_Favoritos")

class Personajes_Favoritos(Base):
    __tablename__ = "personajes_favoritos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    personaje_id = Column(Integer, ForeignKey("personajes.id"))



class Planetas_Favoritos(Base):
    __tablename__ = "planetas_favoritos"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    planeta_id = Column(Integer, ForeignKey("planetas.id"))

class Personajes(Base):
    __tablename__ = "personajes"
    # Here we define columns for the table personajes
    id = Column(Integer, primary_key=True)
    # favoritos_id = Column(Integer, ForeignKey("favoritos.id"))
    name = Column(String(250), nullable=False)
    clasificacion = Column(String(250), nullable=False)
    lenguaje = Column(String(250), nullable=False)
    creacion = Column(String(250), nullable=False)
    favoritos = relationship("Personajes_Favoritos")

class Planetas(Base):
    __tablename__ = "planetas"
    # Here we define columns for the table personajes
    id = Column(Integer, primary_key=True)
    # favoritos_id = Column(Integer, ForeignKey("favoritos.id"))
    name = Column(String(250), nullable=False)
    gravedad = Column(String(250), nullable=False)
    favoritos = relationship("Planetas_Favoritos")

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')