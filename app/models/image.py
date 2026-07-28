from datetime import datetime
from app.extensions import db


class AnalysisImage(db.Model):
    __tablename__ = "analysis_images"

    id = db.Column(db.Integer, primary_key=True)

    analysis_id = db.Column(
        db.Integer,
        db.ForeignKey("analysis.id"),
        nullable=False
    )

    image_type = db.Column(
        db.String(50),
        nullable=False
    )

    filename = db.Column(
        db.String(255),
        nullable=False
    )

    uploaded_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Image {self.filename}>"