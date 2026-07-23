from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.routes.analysis import analysis

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(analysis)

    app.config["SECRET_KEY"] = "tradepilot"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tradepilot.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    with app.app_context():
    db.create_all()

    @app.route("/")
    def dashboard():
        return render_template("dashboard.html")

    return app