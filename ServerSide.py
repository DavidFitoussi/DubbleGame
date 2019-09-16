from flask import Flask
from flask_restful import Api, Resource , reqparse
from flask_cors import CORS
from Double import clsGame
import json

app  = Flask(__name__)
CORS(app)
api = Api(app)

class Service (Resource):
    @app.route('/index')
    def index():
        return "Hello, david!"

    @app.route('/GetCard')
    def GetCard():
        InstanceResource = clsGame()
        InstanceResource.InitMatrix()
        result = json.dumps(InstanceResource.Card)
        return result,200

api.add_resource(Service)

app.run(debug=True)


