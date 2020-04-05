from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

from app.schemes.dummy_schema import DummySchema, DummyReturnSchema

ns = Namespace('dummy', description="Dummy")

@ns.route('/hello/world')
class HelloWorldResource(Resource):
    @accepts(schema=DummySchema, api=ns)
    @responds(schema=DummyReturnSchema, status_code=201, api=ns)
    def post(self):
        #TODO: receive json, put it to the model, save into db, return
        return None
