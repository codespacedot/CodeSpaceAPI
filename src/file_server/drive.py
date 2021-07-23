"""Deta Drive operations.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '23/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Optional
from fastapi import UploadFile

# Own Imports
from src.settings import DRIVE_IMAGE, DRIVE_DOC
from src.utils import string_utils


class Drive(object):
    """Drive class for Deta drive operations.

    Parameters:
        type_: Type of drive [image, document]
    """

    def __init__(self, type_: str):
        if type_ == 'image':
            self.drive = DRIVE_IMAGE
        else:
            self.drive = DRIVE_DOC

    def upload(self, file: UploadFile, key: str) -> Optional[str]:
        """Upload file to drive.

        Arguments:
        ---------
            file: file to upload.
            key: User's database key.

        Returns:
        ---------
            Name of the file if uploaded else None.
        """
        filename = file.filename
        filename = string_utils.file_name(name=filename, key=key)
        try:
            return self.drive.put(name=filename, data=file.file)
        except Exception:  # Type of exception is not provided by deta.
            return

    def download(self, filename: str):
        """Download file from drive.

        Arguments:
        ---------
            filename: Name of the image file to download.

        Returns:
        ---------
            File data of type `DriveStreamingBody` if exists else None.
        """
        return self.drive.get(name=filename)

    def delete(self, filename: str) -> Optional[str]:
        """Delete file from drive.

        Arguments:
        ---------
            filename: Name of the image file to delete.

        Returns:
        ---------
            Name of the file if deleted else None.
        """
        try:
            return self.drive.delete(name=filename)
        except Exception:  # Type of exception is not provided by deta.
            return
