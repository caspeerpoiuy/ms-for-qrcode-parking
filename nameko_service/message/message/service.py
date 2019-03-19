from nameko.rpc import rpc


class MessageService(object):
    name = "message_service"

    @rpc
    def send_sms(self, to):
        print(to)
        return to

    @rpc
    def send_mail(self, to):
        pass

    @rpc
    def store_code(self, code):
        print(code)