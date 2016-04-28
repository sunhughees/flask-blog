import falcon

class Resource(object):

    def __init__(self, storage_path):
        self.storage_path = storage_path

    def on_get(self, req, resp):
        resp.body = '{"message": "Hello world!"}'
        resp.status = falcon.HTTP_200

