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

YEAR_MAP = {'second': 2, 'third': 3, 'final': 4}  # Mapping year to int


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


def get_subjects(year: Optional[str] = None) -> Union[List[Dict], None]:
    """Fetch list of subjects.

    Fetch subjects for specified year if no year, fetch all.

    Arguments:
    ---------
        year: Academics year.

    Returns:
    ---------
        List of Dictionaries for each subject.
    """
    if not year:
        return next(SUBJECTS.fetch())
    try:
        return next(SUBJECTS.fetch({'year': YEAR_MAP[year]}))
    except KeyError:
        return None


def get_labs(year: Optional[str] = None) -> Union[List[Dict], None]:
    """Fetch list of labs.

    Fetch labs for specified year if no year, fetch all.

    Arguments:
    ---------
        year: Academics year.

    Returns:
    ---------
        List of Dictionaries for each lab.
    """
    if not year:
        return next(LABS.fetch())
    try:
        return next(LABS.fetch({'year': YEAR_MAP[year]}))
    except KeyError:
        return None
