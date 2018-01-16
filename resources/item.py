from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


# create a resource
class Item(Resource):
    # create a parser object
    parser = reqparse.RequestParser()
    # add agruments to the parser object
    parser.add_argument('price', type=float, required=True, help="Please define 'price'")
    parser.add_argument('store_id', type=int, required=True, help="Please mention the store id for the item")


    @jwt_required()  # verify token when the user sends a 'GET' request for an item
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"message": "Item already exists"}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred while inserting the item"}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "Item successfully deleted"}
        return {"message": "No such item found to delete"}

    def put(self, name):
        # parse arguments and store it in a variable
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            item.price = data['price']
            item.store_id = data['store_id']
        else:
            item = ItemModel(name, data['price'], data['store_id'])
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    @jwt_required()
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
        #return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}
