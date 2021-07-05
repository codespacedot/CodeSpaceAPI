from fastapi import FastAPI
from .routes import academics

app = FastAPI(title='CodeSpace API', description='API for csdot.ml', version='0.1', docs_url='/')

app.include_router(academics.router)
