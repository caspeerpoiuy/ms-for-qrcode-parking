import json
from nameko.rpc import RpcProxy
from entrypoints import http
from schemas import RegisterUserSchema, LoginUserSchema
from utils import generate_token, resolute_token
from captcha.captcha.captcha import captcha
from werkzeug.wrappers import Response


class GatewayService(object):
    name = "gateway_service"
    message_service_rpc = RpcProxy("message_service")
    user_service_rpc = RpcProxy("user_service")

    @http("GET", "/image")
    def captcha_service(self, request):
        image_id = request.args.get("image_id")
        _, code, image = captcha.generate_captcha()
        self.message_service_rpc.store_code.call_async(image_id, code)
        return Response(
            image,
            mimetype='img/jpg'
        )

    @http("POST", "/sms")
    def send_sms_service(self, request):
        is_success = self.message_service_rpc.send_sms.call_async((request.get_data(as_text=True)))
        return json.dumps({"message": "ok", "code": 200})

    @http("POST", "/login")
    def login_service(self, request):
        schema = LoginUserSchema(strict=True)
        try:
            user_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as e:
            print(e)
        user = self._login_user(user_data)
        token = generate_token(user)
        return token

    def _login_user(self, user_data):
        return self.user_service_rpc.login_user(user_data)

    @http("POST", "/register")
    def register_service(self, request):
        schema = RegisterUserSchema(strict=True)
        try:
            user_data = schema.loads(request.get_data(as_text=True)).data
        except ValueError as e:
            print(e)
        user = self._create_user(user_data)
        token = generate_token(user)
        return token

    def _create_user(self, user_data):
        return self.user_service_rpc.create_user(user_data)

    @http("get", "/user")
    def get_user(self, request):
        token = request.args.get("token")
        id, username = resolute_token(token)
        user = self._get_user(id)
        return user.get("username")

    def _get_user(self, id):
        return self.user_service_rpc.get_user(id)
