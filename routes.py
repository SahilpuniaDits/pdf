
from flask_restful import Api
from convert import index

def initialize_routes(app):
    api = Api(app)
    api.add_resource(index,'/api/pdf/<file>')