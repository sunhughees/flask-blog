import falcon
import images

api = application = falcon.API()

storage_path = '/home/sven/Desktop/sundapeng/flask-blog/falcon/look/storage/'

images = images.Resource(storage_path)

api.add_route('/images', images)
