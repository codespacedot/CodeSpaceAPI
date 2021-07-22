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
from . import image_drive

fs_router = APIRouter(prefix='/files', tags=['File server'])

# TODO: @fs_router.get('/document/{filename}')


@fs_router.get('/image/{filename}', status_code=status.HTTP_200_OK)
async def get_image(filename: str):
    """Download image."""
    image = image_drive.download_image(filename=filename)
    if not image:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'ERROR': 'File not found.'})
    return StreamingResponse(image.iter_chunks(1024))
