import falcon
import images

api = application = falcon.API()

storage_path = '/home/sven/Desktop/sundapeng/flask-blog/falcon/look/storage/'

image_collection = images.Collection(storage_path)
image_item = image.Item(storage_path)

api.add_route('/images', image_collection)
api.add_route('/images/(name)', image_item)
