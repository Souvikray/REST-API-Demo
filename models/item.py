from db import db


class ItemModel(db.Model):
    # instruct sqlalchemy to use the 'items' table
    __tablename__ = 'items'

    # map the objects to the database
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    # create a relation with the store model
    store = db.relationship('StoreModel')
    # each item belongs to a store
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {"name": self.name, "price": self.price, "store_id": self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()  # SELECT * FROM items WHERE name=name # fetch the first row

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
