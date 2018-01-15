from flask_restful import Resource, reqparse
from code_flask2.models.user import UserModel


class UserRegister(Resource):
    # declare parser as class variable
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="Please provide a username")
    parser.add_argument("password", type=str, required=True, help="Please provide a password")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that name already exists"}, 400
        #user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()
        return {"message": "User created successfully"}
