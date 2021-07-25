"""Router for Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

from typing import Dict

# Library Imports
from fastapi import APIRouter, Depends, File, Form, UploadFile, status

from src.users import oauth2
# Own Imports
from . import main, models

academic_router = APIRouter(prefix='/api/academics', tags=['Academics'])


@academic_router.get('/year/{year}', response_model=models.Year, status_code=status.HTTP_200_OK)
async def data_for_year(year: int):
    """Get subjects and labs for specified academic year.

    YEAR = [2, 3, 4]
    ----
    """
    return main.get_data_for_year(year)


@academic_router.post('/resources/upload', status_code=status.HTTP_200_OK)
async def upload_resource(subject: str = Form(...), title: str = Form(...), category: str = Form(...),
                          document: UploadFile = File(...), user: Dict = Depends(oauth2.get_current_user)):
    """Upload resource."""
    return main.upload_resource(user=user, subject=subject, title=title, category=category, document=document)


@academic_router.get('/resources/{subject_code}', response_model=models.Resources, status_code=status.HTTP_200_OK)
async def get_subject_resources(subject_code: str):
    """Get resources of a subject."""
    return main.get_resources(subject=subject_code)
