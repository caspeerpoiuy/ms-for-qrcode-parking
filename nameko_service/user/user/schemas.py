from marshmallow import Schema, fields, post_load
from models import UserModel


class CreateUserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    mobile = fields.Integer(required=True)

    @post_load
    def make_user(self, data):
        return UserModel(**data)


class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.String(required=True)

