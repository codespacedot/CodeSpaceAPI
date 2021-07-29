"""Document drive.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '23/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import UploadFile
from typing import Optional

# Own Imports
from .base_drive import Drive

drive = Drive(type_='document')


def upload_document(document: UploadFile, key: str) -> Optional[str]:
    """Upload document to Deta drive.

    Arguments:
    ---------
        document: document file.
        key: User's database key.

    Returns:
    ---------
        Name of the file if uploaded else None.
    """
    return drive.upload(file=document, key=key)


def download_document(filename: str):
    """Download document from drive.

    Arguments:
    ---------
        filename: Name of the image file to download.

    Returns:
    ---------
        File data of type `DriveStreamingBody` if exists else None.
    """
    return drive.download(filename=filename)


def delete_document(filename: str) -> Optional[str]:
    """Delete document from drive.

    Arguments:
    ---------
        filename: Name of the image file to delete.

    Returns:
    ---------
        Name of the file if deleted else None.
    """
    return drive.delete(filename=filename)
