from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

SECRET_KEY = "jdaksjdasljdas"

def generate_token(user):
    serializer = Serializer(SECRET_KEY)
    return serializer.dumps({"id": user["id"], "username": user["username"]}).decode()


def resolute_token(token):
    serializer = Serializer(SECRET_KEY)
    id = serializer.loads(token).get("id")
    username = serializer.loads(token).get("username")
    return id, username