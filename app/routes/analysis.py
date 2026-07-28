from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
)

from app.extensions import db
from app.models.analysis import Analysis
from app.models.image import AnalysisImage
from app.services.upload_service import UploadService
from flask import send_from_directory
import os

analysis_bp = Blueprint(
    "analysis",
    __name__
)

@analysis_bp.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(
        UploadService.UPLOAD_FOLDER,
        filename
    )
@analysis_bp.route(
    "/analysis/<int:analysis_id>/delete/<image_type>",
    methods=["POST"]
)
def delete_image(analysis_id, image_type):

    image = AnalysisImage.query.filter_by(
        analysis_id=analysis_id,
        image_type=image_type
    ).first_or_404()

    file_path = os.path.join(
        UploadService.UPLOAD_FOLDER,
        image.file_path
    )

    if os.path.exists(file_path):
        os.remove(file_path)

    db.session.delete(image)
    db.session.commit()

    return redirect(
        url_for(
            "analysis.workspace",
            analysis_id=analysis_id
        )
    )
# ----------------------------------------------------
# Create New Analysis
# ----------------------------------------------------
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


# ----------------------------------------------------
# Analysis Workspace
# ----------------------------------------------------
@analysis_bp.route("/analysis/<int:analysis_id>")
def workspace(analysis_id):

    analysis = Analysis.query.get_or_404(analysis_id)

    images = {
        image.image_type: image
        for image in analysis.images
    }

    return render_template(
        "analysis.html",
        analysis=analysis,
        images=images
    )


# ----------------------------------------------------
# Upload Image
# ----------------------------------------------------
@analysis_bp.route(
    "/analysis/<int:analysis_id>/upload",
    methods=["POST"]
)
def upload_image(analysis_id):

    analysis = Analysis.query.get_or_404(analysis_id)

    image = request.files.get("image")

    if image is None or image.filename == "":
        return redirect(
            url_for(
                "analysis.workspace",
                analysis_id=analysis.id
            )
        )

    image_type = request.form.get("image_type")

    filepath = UploadService.save(
        file=image,
        analysis_id=analysis.id,
        image_type=image_type
    )

    existing_image = AnalysisImage.query.filter_by(
        analysis_id=analysis.id,
        image_type=image_type
    ).first()

    if existing_image:

        existing_image.file_path = filepath
        existing_image.original_filename = image.filename

    else:

        new_image = AnalysisImage(
            analysis_id=analysis.id,
            image_type=image_type,
            file_path=filepath,
            original_filename=image.filename
        )

        db.session.add(new_image)

    db.session.commit()

    return redirect(
        url_for(
            "analysis.workspace",
            analysis_id=analysis.id
        )
    )