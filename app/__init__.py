from flask import Flask
from config import Config
from dal.db import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app
