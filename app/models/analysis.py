from datetime import datetime
from app.extensions import db


class Analysis(db.Model):
    __tablename__ = "analysis"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(
        db.String(100),
        nullable=False,
        default="New Analysis"
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="Draft"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    images = db.relationship(
        "AnalysisImage",
        backref="analysis",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Analysis {self.id}>"