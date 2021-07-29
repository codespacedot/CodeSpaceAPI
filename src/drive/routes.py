"""Router for File server.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '22/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import StreamingResponse

# Own Imports
from . import document_drive, image_drive

drive_router = APIRouter(prefix='/drive', tags=['Drive'])


@drive_router.get('/document/{filename}', status_code=status.HTTP_200_OK)
async def get_document(filename: str):
    """Download document."""
    document = document_drive.download_document(filename=filename)
    if not document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'ERROR': 'File not found.'})
    return StreamingResponse(document.iter_chunks(1024))


@drive_router.get('/image/{filename}', status_code=status.HTTP_200_OK)
async def get_image(filename: str):
    """Download image."""
    image = image_drive.download_image(filename=filename)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'ERROR': 'File not found.'})
    return StreamingResponse(image.iter_chunks(1024))
