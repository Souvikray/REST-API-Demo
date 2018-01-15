from app import app
from db import db

# create a database before flask starts accepting requests
@app.before_first_request
def create_tables():
    db.create_all()
# enable sqlalchemy to use the flask app
db.init_app(app)
