import os
from flask import Flask
from .routes import matching_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World f!</p>"

    app.register_blueprint(matching_bp)
    return app
