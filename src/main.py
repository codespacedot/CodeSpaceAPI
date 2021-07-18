"""App of FastAPI.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '06/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Own Imports
from .academics.routes import academic_router
from .users.routes import user_router
from .settings import ALLOWED_ORIGINS

# FastAPI app
app = FastAPI(title='CodeSpace API', description='API for csdot.ml', version='0.2.1', docs_url='/')


app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(user_router)  # User API
app.include_router(academic_router)  # Academic API
