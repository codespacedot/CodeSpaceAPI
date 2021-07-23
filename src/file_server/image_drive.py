"""Image drive.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '22/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import UploadFile
from typing import Optional

# Own Imports
from .drive import Drive

drive = Drive(type_='image')


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
    return drive.upload(file=image, key=key)


def download_image(filename: str):
    """Download image from drive.

    Arguments:
    ---------
        filename: Name of the image file to download.

    Returns:
    ---------
        File data of type `DriveStreamingBody` if exists else None.
    """
    return drive.download(filename=filename)


def delete_image(filename: str) -> Optional[str]:
    """Delete image from drive.

    Arguments:
    ---------
        filename: Name of the image file to delete.

    Returns:
    ---------
        Name of the file if deleted else None.
    """
    return drive.delete(filename=filename)
