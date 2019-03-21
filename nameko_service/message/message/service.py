from nameko.rpc import rpc
from dependencies import Storage


class MessageService(object):
    name = "message_service"
    storage = Storage()

    @rpc
    def send_sms(self, to):
        print(to)
        #TODO: expend function of send sms code

    @rpc
    def send_mail(self, to):
        pass

    @rpc
    def store_code(self, image_id, code):
        status = self.storage.create(image_id, 120, code)
        print(status)