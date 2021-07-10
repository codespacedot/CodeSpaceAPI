"""Main functionalities of Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import HTTPException, status
from typing import Dict

# Own Imports
from . import db


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
        HTTPException 404 if year is invalid.
    """
    subjects = db.get_subjects(year=year)
    labs = db.get_labs(year=year)

    if not subjects or not labs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
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
