from werkzeug.security import safe_str_cmp

from code_flask2.models.user import UserModel


# when the user sends its credentials, it will be checked against the registered users
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):  # to avoid string comparison issues in some systems
        return user

# once the authentication is successful, the token generated is sent and stored at the user's system.
# when the next time the user sends a request, the token is sent as well and validated against using
# the below function
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


