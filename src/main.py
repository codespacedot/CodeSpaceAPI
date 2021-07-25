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
from src.settings import ALLOWED_ORIGINS
from src.academics.routes import academic_router
from src.file_server.routes import fs_router
from src.users.routes import user_router

# FastAPI app
app = FastAPI(title='CodeSpace API', description='API for csdot.ml', version='Beta 1.0', docs_url='/')

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
app.include_router(fs_router)  # File server
