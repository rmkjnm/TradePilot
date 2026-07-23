import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = "uploads"


def save_file(file):

    if file.filename == "":
        return None

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(filepath)

    return filepath