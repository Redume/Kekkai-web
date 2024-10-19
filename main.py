import uvicorn
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from fastapi import FastAPI

from src.routes import index

app = FastAPI()
app.include_router(index.router)
app.mount('/static/', StaticFiles(directory='./src/web/static/'))


@app.exception_handler(404)
async def not_found(req, __):
    return FileResponse('./src/web/errors/404.html')

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9000)
