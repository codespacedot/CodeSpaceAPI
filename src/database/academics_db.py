"""Database operations for Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Dict, List, Optional

# Own Imports
from src.settings import BASE_SUBJECT, BASE_LAB


def get_subject(code: str) -> Dict:
    """Fetch subject with matching code.

    Arguments:
    ---------
        code: Subject code.

    Returns:
    ---------
        Dictionary if subject with the code is present else None.
    """
    return BASE_SUBJECT.get(key=code)


def get_subjects(year: Optional[int] = -1) -> Optional[List[Dict]]:
    """Fetch list of subjects.

    Fetch subjects for specified year if year is -1, fetch all.

    Arguments:
    ---------
        year: Academics year.

    Returns:
    ---------
        List of Dictionaries for each subject.
    """
    if not year:
        return next(BASE_SUBJECT.fetch())
    if year not in {2, 3, 4}:
        return None
    return next(BASE_SUBJECT.fetch(query={'year': year}))


def get_labs(year: Optional[int] = -1) -> Optional[List[Dict]]:
    """Fetch list of labs.

    Fetch labs for specified year if year is -1, fetch all.

    Arguments:
    ---------
        year: Academics year.

    Returns:
    ---------
        List of Dictionaries for each lab.
    """
    if year == -1:
        return next(BASE_LAB.fetch())
    if year not in {2, 3, 4}:
        return None
    return next(BASE_LAB.fetch(query={'year': year}))
