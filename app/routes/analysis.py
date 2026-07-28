from flask import Blueprint, render_template, redirect, url_for

from app.extensions import db
from app.models.analysis import Analysis

analysis_bp = Blueprint(
    "analysis",
    __name__
)


@analysis_bp.route("/new-analysis")
def new_analysis():

    analysis = Analysis()

    db.session.add(analysis)

    db.session.commit()

    return redirect(
        url_for(
            "analysis.workspace",
            analysis_id=analysis.id
        )
    )


@analysis_bp.route("/analysis/<int:analysis_id>")
def workspace(analysis_id):

    analysis = Analysis.query.get_or_404(
        analysis_id
    )

    return render_template(
        "analysis.html",
        analysis=analysis
    )