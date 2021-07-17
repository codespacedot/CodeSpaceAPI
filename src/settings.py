"""Settings for projects.
Contains configurations and environment variables
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from decouple import config

# Deta
DETA_ACCESS_KEY = config('DETA_ACCESS_KEY')

BASE_SUBJECT = 'subject'
BASE_LAB = 'lab'
BASE_USER = 'user'
BASE_PROFILE = 'profile'
BASE_PASSWORD_RESET = 'pReset'

# JWT
JWT_SECRET_KEY = config('JWT_SECRET_KEY')
JWT_ALGORITHM = 'HS256'
JWT_EXPIRE_MINUTES = 30

# Mail
MAIL_ID = config('MAIL_ID')
MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_PORT = 587
MAIL_SERVER = 'smtp.gmail.com'
MAIL_TEMPLATES_PATH = './templates/email'


# PyTest User
class TestUser(object):
    """Used to test User APIs"""
    EMAIL = config('TEST_EMAIL')
    F_NAME = 'PyTest'
    L_NAME = 'FastAPI'
    DOB = '15041984'
    PASSWORD = 'password'
    BATCH = '2020'
    BIO = 'Default bio.'
    LINKEDIN = 'Link to linkedin profile'
    GITHUB = 'Link to GitHub profile'
    SKILLS = ['python', 'fastapi']


# Verification
VERIFICATION_CODE_LENGTH = 6
