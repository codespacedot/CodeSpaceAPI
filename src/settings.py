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

# JWT
JWT_SECRET_KEY = config('JWT_SECRET_KEY')
JWT_ALGORITHM = config('JWT_ALGORITHM')
JWT_EXPIRE_MINUTES = config('JWT_EXPIRE_MINUTES', cast=int)
