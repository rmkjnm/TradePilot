from datetime import datetime

from app.extensions import db


class OCRResult(db.Model):

    __tablename__ = "ocr_results"

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

    raw_text = db.Column(
        db.JSON,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )