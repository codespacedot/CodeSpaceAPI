"""App of FastAPI.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '06/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import FastAPI

# Own Imports
from .academics.routes import academic_router
from .users.routes import user_router

# FastAPI app
app = FastAPI(title='CodeSpace API', description='API for csdot.ml', version='0.2.1', docs_url='/')

# Routers
app.include_router(user_router)  # User API
app.include_router(academic_router)  # Academic API
