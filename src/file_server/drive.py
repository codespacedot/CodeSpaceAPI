from fastapi import UploadFile
from deta import Deta
from src import settings
from src.utils import string_utils

deta = Deta(settings.DETA_ACCESS_KEY)
DRIVE = deta.Drive(settings.DRIVE_IMAGE)


def upload_image(image: UploadFile, key: str):
    f_name = image.filename
    f_name = string_utils.file_name(name=f_name, key=key)
    return DRIVE.put(name=f_name, data=image.file)


def download_image():
    pass


def delete_image():
    pass
