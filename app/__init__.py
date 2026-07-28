from flask import Flask, render_template

from app.extensions import db

from app.routes.analysis import analysis_bp


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "tradepilot"

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tradepilot.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(analysis_bp)

    with app.app_context():
        db.create_all()

    @app.route("/")
    def dashboard():
        return render_template("dashboard.html")

    return app