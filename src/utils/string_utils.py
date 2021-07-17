"""String utilities.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '17/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
import string
import random

# Own Imports
from .. import settings


def verification_code() -> str:
    """Generate verification code.

    Returns:
    ---------
        Alphanumeric code of length 'src.settings.VERIFICATION_CODE_LENGTH'
    """
    data = string.ascii_uppercase + string.digits
    code = ''.join([random.choice(data) for _ in range(settings.VERIFICATION_CODE_LENGTH)])

    return code
