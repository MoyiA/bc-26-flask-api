from flask import Flask
from flask_restful import Api
from flask import make_response, jsonify

from main.config import DevelopmentConfig, TestingConfig, ProductionConfig, StagingConfig
from main.api import Books

def create_app(config_name):
    # intialize app
    app = Flask(__name__)

    # load configuration
    if config_name == 'develop':
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
    elif config_name == 'production':
        app.config.from_object(ProductionConfig)
    elif config_name == 'staging':
        app.config.from_object(StagingConfig)
    else:
        return "error"

    # extend flask to handle resp api
    api = Api(app)

    #add url resources
    api.add_resource(Books, "/api/v1/books")

    # add error handling
    @app.errorhandler(404)
    def not_found(e):
        response = jsonify({"message":"error, resource not found"})
        return response, 404

    @app.errorhandler(500)
    def internal_server_error(e):
        response = jsonify({"message":"error, internal server error"})
        return response, 500

    return app

