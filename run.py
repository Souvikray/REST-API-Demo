from app import app
from db import db

# enable sqlalchemy to use the flask app
db.init_app(app)
# create a database before flask starts accepting requests
@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    return render_template('welcome.html')
