from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


@router.get('/')
async def main():
    return FileResponse('./src/web/page/index.html')
