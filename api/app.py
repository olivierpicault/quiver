from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from config import Config
from database import db
from src.controllers.board_controller import board_controller
from src.models.board import Board


def create_app(config):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(board_controller)

    app.url_map.strict_slashes = False

    return app


app = create_app(Config)

board = Board()
