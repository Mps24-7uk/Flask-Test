from models.item import ItemModel
from flask_restful import Resource, reqparse
import sqlite3


class Item(Resource):
    

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.jsonn()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}

        return item.jsonn(),201
   
    def delete(self, name):
        item=ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'Msg':'Item Deleted'}
        return {'Msg':'Item Not found'},404

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
    
        if item is None:
            item= ItemModel(name,data['price'])
        else:
            item.price=data['price']

        item.save_to_db()
        
        return item.jsonn() 




class ItemList(Resource):
    def get(self):
        return {'items':[item.jsonn() for item in ItemModel.query.all()]}
      #  return {'item':list(map(lambda item: item.jsonn(),ItemModel.query.all()))}
