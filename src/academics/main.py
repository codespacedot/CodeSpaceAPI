"""Main functionalities of Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Dict, List
from fastapi import HTTPException, UploadFile, status

# Own Imports
from src import settings
from src.database import academics_db as db
from src.file_server import document_drive as drive


def get_data_for_year(year: int) -> Dict:
    """Get subjects and labs for specified year.

    Arguments:
    ---------
        year: Academic year.

    Returns:
    ---------
        Dictionary containing dictionary for each semester.

    Raises:
    ---------
        HTTPException 400 if year is invalid.
    """
    subjects = db.get_subjects(year=year)
    labs = db.get_labs(year=year)

    if not subjects or not labs:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail={'ERROR': 'Invalid Year', 'MESSAGE': 'Use 2, 3 or 4'})

    data = {
        'ODD_SEMESTER': {
            'SUBJECTS': [],
            'LABS': []
        },
        'EVEN_SEMESTER': {
            'SUBJECTS': [],
            'LABS': []
        }
    }

    for subject in subjects:
        if subject['semester'] % 2:
            data['ODD_SEMESTER']['SUBJECTS'].append(subject)
        else:
            data['EVEN_SEMESTER']['SUBJECTS'].append(subject)

    for lab in labs:
        if lab['semester'] % 2:
            data['ODD_SEMESTER']['LABS'].append(lab)
        else:
            data['EVEN_SEMESTER']['LABS'].append(lab)

    return data


def get_subjects(semester: int) -> List[Dict]:
    """Get subjects for specified semester.

    Arguments:
    ---------
        semester: Semester [3...8].

    Returns:
    ---------
        List of subject dictionaries.

    Raises:
    ---------
        HTTPException 400 if semester is invalid.
        HTTPException 500 if drive/database error.
    """
    if semester not in range(3, 9):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'ERROR': 'Invalid semester.'})
    subjects = db.get_subject_of_sem(semester=semester)
    if not subjects:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'ERROR': 'Internal Error.'})
    return subjects


def upload_resource(user: Dict, subject: str, title: str, category: str, document: UploadFile) -> Dict:
    """Upload resource.

    Arguments:
    ---------
        user: User dictionary.
        subject: Subject code.
        title: Resource title.
        category: Type of resource. [library, exam]
        document: Document file.

    Returns:
    ---------
        Success Dictionary.

    Raises:
    ---------
        HTTPException 400 if subject is invalid.
        HTTPException 400 if category is invalid.
        HTTPException 500 if drive/database error.
    """
    all_subjects = db.get_subjects()
    subject_codes = {sub['key'] for sub in all_subjects}

    if subject not in subject_codes:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'ERROR': 'Invalid subject code.'})

    if category not in {'library', 'exam'}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'ERROR': 'Invalid category.'})

    filename = drive.upload_document(document=document, key=user['key'])
    if not filename:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'ERROR': 'Internal Error.'})
    url = settings.DOCUMENT_SERVER_PATH + filename
    if not db.create_resource(subject=subject, title=title, category=category, user=user['key'], url=url):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'ERROR': 'Internal Error.'})
    return {'detail': 'Resource uploaded.'}


def get_resources(subject: str):
    """Get resources of a subjects.

    Arguments:
    ---------
        subject: Subject code.

    Returns:
    ---------
        Dictionary containing lists resources for each type.

    Raises:
    ---------
        HTTPException 404 if resources not available.
    """
    resources = db.get_resources(subject=subject)
    if not resources:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'ERROR': 'No resources.'})

    data = {
        'LIBRARY': [],
        'EXAM': []
    }

    for resource in resources:
        if resource['category'] == 'library':
            data['LIBRARY'].append(resource)
        else:
            data['EXAM'].append(resource)

    print(data)
    return data
