from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel


# create a resource
class Store(Resource):
    # create a parser object
    parser = reqparse.RequestParser()
    # add agruments to the parser object
    parser.add_argument('name', type=float, required=True, help="Please define 'price'")

    @jwt_required()  # verify token when the user sends a 'GET' request for a store
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message": "Store already exists"}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred while inserting the item"}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            # delete all the items associated with the store
            for item in store.items.all():
                item.delete_from_db()
            # finally delete the store
            store.delete_from_db()
            return {"message": "Item successfully deleted"}
        return {"message": "No such item found to delete"}


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
        #return {"stores": list(map(lambda x: x.json(), StoreModel.query.all()))}
