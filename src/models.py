import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'newUser'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    userName = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def serialize (self):
        return{
            "email": self.email,
            "userName": self.userName,
        }

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    diameter = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)
    climate = Column(String(250), nullable=True) 

    def serialize(self):
        return {
            "diameter":self.diameter,
            "mass": self.mass,
            "climate": self.climate,
        }

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    manufacturer = Column(String(250), nullable=True)
    model = Column(String(250), nullable=True)
    cost_in_credits = Column(String(250), nullable=True) 

    def serialize(self):
        return {
            "manufacturer": self.manufacturer,
            "model": self.model,
            "cost_in_credits": self.cost_in_credits,
        }   

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    height = Column(String(250), nullable=True)
    mass = Column(String(250), nullable=True)

    def serialize(self):
        return {
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
        }

class Favorties(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'), nullable=True)
    character_id= Column(Integer,ForeignKey('character.id'), nullable=True)
    vehicle_id = Column(Integer,ForeignKey('vehicle.id'), nullable=True)
    planet_id = Column(Integer,ForeignKey('planet.id'), nullable=True)

    user = relationship(User)
    characters = relationship(Characters)
    Vehicles = relationship(Vehicles)
    Planets = relationship(Planets)

    def serialize(self):
        return {
            "user_id": self.user_id,
            "character_id": self.character_id,
            "vehicle_id": self.vehicle_id,
            "planet_id": self.planet_id,
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
