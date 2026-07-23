from datetime import datetime
from app import db


class Analysis(db.Model):

    __tablename__ = "analysis"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(100),
        default="New Analysis"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(20),
        default="Draft"
    )

    edge_score = db.Column(db.Integer)

    recommendation = db.Column(db.String(50))