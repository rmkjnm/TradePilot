from flask import Blueprint, render_template

analysis = Blueprint("analysis", __name__)


@analysis.route("/analysis")
def upload_page():
    return render_template("analysis.html")