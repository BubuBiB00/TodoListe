# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Todoitem(db.Model):
    __tablename__ = 'todoitems'

    item_ID = db.Column(db.Integer, primary_key=True, unique=True)
    item_name = db.Column(db.String(64))
    item_description = db.Column(db.Text)
