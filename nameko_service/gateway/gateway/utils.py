from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def generate_token(user):
    serializer = Serializer("dsahdjas")
    return serializer.dumps({"id": user["id"], "username": user["username"]}).decode()
