from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Length, Equal


class RegisterUserSchema(Schema):
    username = fields.String(required=True, validate=Length(6, 12))
    password = fields.String(required=True, validate=Length(6, 12))
    confirm_password = fields.String(required=True, validate=Length(6, 12))
    sms_code = fields.String(required=True, validate=Length(equal=4))


class LoginUserSchema(Schema):
    username = fields.String(required=True, validate=Length(6, 12))
    password = fields.String(required=True, validate=Length(6, 12))



