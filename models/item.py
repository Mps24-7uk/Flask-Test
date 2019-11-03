import sqlite3
from db import db

class ItemModel(db.Model):
    __tablename__= 'itemss'
    name=db.Column(db.String(100) ,nullable = False)
    price=db.Column(db.Float(precision=2), nullable = False)
    id = db.Column(db.Integer , primary_key=True , autoincrement=True)

    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def jsonn(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() #ItemModel.query.filter_by

   
    def save_to_db(self): #insert and update both
        db.session.add(self)
        db.session.commit() 

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit() 
