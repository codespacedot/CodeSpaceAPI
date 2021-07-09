"""Database operations using Deta Base SDK.
https://docs.deta.sh/docs/base/sdk
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '06/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from deta import Deta
from decouple import config
from typing import Dict, List, Optional, Union

DB = Deta(config('DATABASE_KEY'))  # Deta access Key
SUBJECTS = DB.Base('subject')  # Base, similar to collection in MongoDB
LABS = DB.Base('lab')


def get_subject(code: str) -> Dict:
    """Fetch subject with matching code.

    Arguments:
    ---------
        code: Subject code.

    Returns:
    ---------
        Dictionary if subject with the code is present else None.
    """
    return SUBJECTS.get(key=code)


def get_subjects(year: Optional[int] = -1) -> Union[List[Dict], None]:
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
        return next(SUBJECTS.fetch())
    if year not in {2, 3, 4}:
        return None
    return next(SUBJECTS.fetch({'year': year}))


def get_labs(year: Optional[int] = -1) -> Union[List[Dict], None]:
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
        return next(LABS.fetch())
    if year not in {2, 3, 4}:
        return None
    return next(LABS.fetch({'year': year}))
