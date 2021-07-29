"""String utilities.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '17/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
import random
import string
from datetime import datetime

# Own Imports
from src import settings


def verification_code() -> str:
    """Generate verification code.

    Returns:
    ---------
        Alphanumeric code of length 'src.settings.VERIFICATION_CODE_LENGTH'
    """
    data = string.ascii_uppercase + string.digits
    code = ''.join([random.choice(data) for _ in range(settings.VERIFICATION_CODE_LENGTH)])

    return code


def file_name(name: str, key: str) -> str:
    """Generate file name.

    Generate a random file name based on current UTC timestamp and specified key.

    Arguments:
    ---------
        name: File name.
        key: Key to add for randomness.

    Returns:
    ---------
        Alphanumeric code of length 'src.settings.VERIFICATION_CODE_LENGTH'
    """
    return datetime.utcnow().strftime(f'%Y%m%d%H%M%S{key}') + '.' + name.split('.')[1]
