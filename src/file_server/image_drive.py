"""Main functionalities of Image drive.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '22/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import UploadFile
from typing import Optional

# Own Imports
from src.settings import DRIVE_IMAGE
from src.utils import string_utils


def upload_image(image: UploadFile, key: str) -> Optional[str]:
    """Upload image to Deta drive.

    Arguments:
    ---------
        image: image file.
        key: User's database key.

    Returns:
    ---------
        Name of the file if uploaded else None.
    """
    filename = image.filename
    filename = string_utils.file_name(name=filename, key=key)
    try:
        return DRIVE_IMAGE.put(name=filename, data=image.file)
    except Exception:  # Type of exception is not provided by deta.
        return


def download_image(filename: str):
    """Download image from Deta drive.

    Arguments:
    ---------
        filename: Name of the image file to download.

    Returns:
    ---------
        File data of type `DriveStreamingBody` if exists else None.
    """
    return DRIVE_IMAGE.get(name=filename)


def delete_image(filename: str) -> Optional[str]:
    """Delete image from Deta drive.

    Arguments:
    ---------
        filename: Name of the image file to delete.

    Returns:
    ---------
        Name of the file if deleted else None.
    """
    try:
        return DRIVE_IMAGE.delete(name=filename)
    except Exception:  # Type of exception is not provided by deta.
        return
