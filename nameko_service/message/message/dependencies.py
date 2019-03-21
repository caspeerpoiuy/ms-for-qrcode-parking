from nameko.extensions import DependencyProvider
import redis

from exceptions import NotFound


REDIS_URI_KEY = 'REDIS_URI'


class StorageWrapper(object):

    NotFound = NotFound

    def __init__(self, client):
        self.client = client

    def create(self, image_id, code, expire_time):
        self.client.setex(image_id, code, expire_time)
        return "OK"


class Storage(DependencyProvider):

    def setup(self):
        self.client = redis.StrictRedis.from_url(
            self.container.config.get(REDIS_URI_KEY))

    def get_dependency(self, worker_ctx):
        return StorageWrapper(self.client)
