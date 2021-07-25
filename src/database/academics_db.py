"""Database operations for Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Dict, List, Optional

# Own Imports
from src.settings import BASE_SUBJECT, BASE_LAB, BASE_RESOURCE


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


def get_subjects(year: Optional[int] = 0) -> Optional[List[Dict]]:
    """Fetch list of subjects.

    Fetch subjects for specified year if year is 0, fetch all.

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


def get_labs(year: Optional[int] = 0) -> Optional[List[Dict]]:
    """Fetch list of labs.

    Fetch labs for specified year if year is 0, fetch all.

    Arguments:
    ---------
        year: Academics year.

    Returns:
    ---------
        List of Dictionaries for each lab.
    """
    if not year:
        return next(BASE_LAB.fetch())
    if year not in {2, 3, 4}:
        return None
    return next(BASE_LAB.fetch(query={'year': year}))


def create_resource(subject: str, title: str, category: str, user: str, url: str) -> bool:
    """Create new resource.

    Arguments:
    ---------
        subject: Subject code.
        title: Resource title.
        category: Type of resource. [library, exam]
        user: User's database key.
        url: Resource file url.

    Returns:
    ---------
        True if resource gets created else False.
    """
    resource = {
        'subject': subject,
        'title': title,
        'category': category,
        'user': user,
        'url': url
    }
    try:
        BASE_RESOURCE.put(resource)
    except Exception as e:
        print(e)
        return False
    return True


def get_resources(subject: str) -> List[Dict]:
    """Fetch resources for a subject.

    Arguments:
    ---------
        subject: Subject code.

    Returns:
    ---------
        List of resource dictionaries with matching subject code.
    """
    return next(BASE_RESOURCE.fetch(query={'subject': subject}))
