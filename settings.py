# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:27:06 2020

@author: user
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False