import falcon
import msgpack


class Resource(object):

    def on_get(self, req, resp):
        resp.data = msgpack.packb({'message': 'Hello world!'})
        resp.content_type = 'application/msgpack'
        resp.status = falcon.HTTP_200

api = application = falcon.API()

say_hi = Resource()

api.add_route('/hi', say_hi)
