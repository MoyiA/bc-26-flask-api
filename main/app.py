from flask import Flask
from flask_restful import Api


from main.config import DevelopmentConfig, TestingConfig, ProductionConfig, StagingConfig



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

    # extend flask
    api = Api(app)

    # add error handling

    return app



