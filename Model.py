# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:23:45 2020

@author: user
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import app
from datetime import datetime
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import json

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', Manager)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def json_1(self):
        return {
               "id": self.id,
               "username": self.username,
               "password": self.password
               }
    def __repr__(self):
        return json.dumps({
                "id": self.id,
                "username": self.username,
                "password": self.password
                }
                )
    def addUser(_username, _password):
        new_user = User(username=_username, password=_password)
        db.session.add(new_user)
        db.session.commit()
        
    def getAllUsers():
        return [User.json_1(user) for user in User.query.all() ]
    
class Contact(db.Model):
    __tablename__="contacts"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    message = db.Column(db.String(250), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def json_1(self):
        return {
               "id": self.id,
               "name": self.name,
               "email": self.email,
               "message": self.message
               }
    def __repr__(self):
        return json.dumps({
                "id": self.id,
                "name": self.name,
                "email": self.email,
                "message": self.message
                }
                )
    def addContact(_name, _email, _message):
        new_contact = Contact(name=_name, email=_email, message=_message)
        db.session.add(new_contact)
        db.session.commit()
        
    def getAllContacts():
        return [Contact.json_1(contact) for contact in Contact.query.all() ]

