from fastapi import FastAPI
import uvicorn

app = FastAPI(title='CodeSpace API', description='api for csdot.ml', version='0.1', docs_url='/')


@app.get('/api')
def index():
    return {'data': 'FastAPI Project'}


if __name__ == '__main__':
    uvicorn.run(app=app)
