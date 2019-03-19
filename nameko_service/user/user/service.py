from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession
from werkzeug.security import generate_password_hash, check_password_hash
from models import DeclarativeBase, UserModel
from schemas import CreateUserSchema, UserSchema
from exceptions import NotFound


class User(object):
    name = "user_service"
    db = DatabaseSession(DeclarativeBase)

    @rpc
    def create_user(self, user_data):
        if self.db.query(UserModel).filter_by(username=user_data.get("username")).first():
            raise ValueError
        schemas = CreateUserSchema()
        user_dict = schemas.load(user_data).data
        user = schemas.make_user(user_dict)
        user.password = generate_password_hash(user.password)
        self.db.add(user)
        self.db.commit()
        return UserSchema().dump(user).data

    @rpc
    def login_user(self, user_data):
        schemas = UserSchema()
        user = self.db.query(UserModel).filter_by(username=user_data.get("username")).first()
        if not user:
            raise NotFound('Order with id {} not found'.format(user_data.get("username")))
        if not check_password_hash(user.password, user_data.get("password")):
            raise ValueError
        return schemas.dump(user).data
