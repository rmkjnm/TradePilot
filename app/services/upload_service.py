import os
from werkzeug.utils import secure_filename


class UploadService:

    UPLOAD_FOLDER = "uploads"

    @staticmethod
    def save(file, analysis_id, image_type):

        folder = os.path.join(
            UploadService.UPLOAD_FOLDER,
            f"analysis_{analysis_id}"
        )

        os.makedirs(folder, exist_ok=True)

        extension = file.filename.rsplit(".", 1)[1].lower()

        filename = f"{image_type}.{extension}"

        filepath = os.path.join(folder, filename)

        file.save(filepath)

        return filepath