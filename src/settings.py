"""Settings for projects.
Contains configurations and secrets.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from decouple import config
from deta import Deta

DEBUG = config('DEBUG', default=False, cast=bool)

if DEBUG:
    HOSTNAME = 'http://localhost:8000'
else:
    HOSTNAME = config('HOSTNAME')

# Allowed Origins
ALLOWED_ORIGINS = config('ALLOWED_ORIGINS').split(',')

# Deta
_DETA = Deta(config('DETA_ACCESS_KEY'))

# Deta Base, similar to collection in MongoDB
BASE_SUBJECT = _DETA.Base('subject')
BASE_LAB = _DETA.Base('lab')
BASE_USER = _DETA.Base('user')
BASE_PROFILE = _DETA.Base('profile')
BASE_PASSWORD_RESET = _DETA.Base('pReset')
BASE_RESOURCE = _DETA.Base('resource')

# Deta Drive
DRIVE_IMAGE = _DETA.Drive('images')
DRIVE_DOC = _DETA.Drive('documents')

IMAGE_SERVER_PATH = HOSTNAME + '/files/image/'
DOCUMENT_SERVER_PATH = HOSTNAME + '/files/document/'

# JWT
JWT_SECRET_KEY = config('JWT_SECRET_KEY')
JWT_ALGORITHM = config('JWT_ALGORITHM')
JWT_EXPIRE_MINUTES = config('JWT_EXPIRE_MINUTES', cast=int)

# Mail
MAIL_ID = config('MAIL_ID')
MAIL_PASSWORD = config('MAIL_PASSWORD')
MAIL_PORT = config('MAIL_PORT', cast=int)
MAIL_SERVER = config('MAIL_SERVER')
MAIL_TEMPLATES_PATH = './templates/email'

# Verification
VERIFICATION_CODE_LENGTH = config('VERIFICATION_CODE_LENGTH', cast=int)


# PyTest User
class TestUser(object):
    """Used to test User APIs"""
    EMAIL = config('TEST_EMAIL')
    F_NAME = 'PyTest'
    L_NAME = 'FastAPI'
    DOB = '15041984'
    PASSWORD = 'password'
    BATCH = '2020'
    BIO = 'bio'
    LINKEDIN = 'https://linkedin.com/in/handle'
    GITHUB = 'https://github.com/handle'
    SKILLS = ['python', 'fastapi']
