from marshmallow import Schema, fields


class RegisterUserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)
    sms_code = fields.String(required=True)


class LoginUserSchema(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
