# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:38:52 2020

@author: user
"""
from Model import User, Contact
from settings import *
import json
import jwt, datetime
from flask import Flask, jsonify, request, Response
from functools import wraps
from flask_cors import CORS

CORS(app)

@app.route("/add/user", methods=["POST"])
def add_user():
    request_data = request.get_json()
    User.addUser(request_data['username'], request_data['password'])
    response = Response("", 200, mimetype='application/json')
    return response

@app.route("/get/users")
def get_all_users():
    return jsonify({ "users": User.getAllUsers() })
    
@app.route("/add/contact", methods=["POST"])
def add_contact():
    request_data = request.get_json()
    Contact.addContact(request_data['name'], request_data['email'], request_data['message'])
    response = Response("", 200, mimetype='application/json')
    return response

@app.route("/get/contacts")
def get_all_contacts():
    return jsonify({ "contacts": Contact.getAllContacts() })
    
    
if __name__ == "__main__":
    app.run()