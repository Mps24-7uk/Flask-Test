from flask import Flask, request
from flask_restful import Api
from resources.item import Item,ItemList

app= Flask(__name__)
api= Api(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.before_first_request
def creat_tables():
	db.create_all()

api.add_resource(Item,'/item/<string:name>')
api.add_resource(ItemList,'/items')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000,debug=True)