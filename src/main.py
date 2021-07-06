"""App of FastAPI.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '06/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import FastAPI

# Own Imports
from .routes import academics

# FastAPI app
app = FastAPI(title='CodeSpace API', description='API for csdot.ml', version='0.1', docs_url='/')

# Routers
app.include_router(academics.router)  # Academic API
